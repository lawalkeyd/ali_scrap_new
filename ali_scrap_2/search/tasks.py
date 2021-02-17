from celery import task

@task()
def crawl_domain(url):
    from .crawl import url_crawl
    return url_crawl(url)