from playwright.sync_api import sync_playwright
from app.services.skill_extractor import extract_skills
import time

_cached_jobs = []
_last_fetch = 0

def fetch_jobs_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://justjoin.it/all-locations/python")
        page.wait_for_timeout(5000)

        texts = page.locator("div").all_inner_texts()

        def is_valid_job(text):
            if not text:
                return False
            
            lines = []

            for l in text.split("\n"):
                if l.strip():
                    lines.append(l.strip())

            if len(lines) < 3:
                return False
            
            title = lines[0]

            if "python" not in title.lower():
                return False
            
            blacklist = [
                "Search",
                "Subscribe",
                "Job offers",
                "AI/ML",
                "We’re hiring",
                "Super offer",
                "Remote",
                "Location"
            ]
            if any(b in title for b in blacklist):
                return False
            if "left" in title.lower():
                return False
            
            return True
        
        def is_company(line):
            blacklist = [
                "PLN", "left", "Remote", "Location",
                "Warszawa", "Kraków", "Wrocław", "Gdańsk", "Salary"
            ]


            if any(char.isdigit() for char in line):
                return False

            if any(b in line for b in blacklist):
                return False

            return True

        def parse_job(text):
            lines = []

            for l in text.split("\n"):
                if l.strip():
                    lines.append(l.strip())

            title = lines[0]
            company = "unknown"
            
            for line in lines:
                if line == title:
                    continue
                if is_company(line):
                    company = line
                    break

            return {
                "title": title,
                "company": company,
                "description": text,
                "skills": extract_skills(text)
            }

        seen = set()
        jobs = []

        for text in texts:
            if not is_valid_job(text):
                continue

            job = parse_job(text)

            if job["title"] in seen:
                continue

            seen.add(job["title"])
            jobs.append(job)

        return jobs[:20]
def get_jobs_cached():
    global _cached_jobs, _last_fetch

    if time.time() - _last_fetch > 300:
        _cached_jobs = fetch_jobs_playwright()
        _last_fetch = time.time()

    return _cached_jobs
