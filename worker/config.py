from celery.schedules import crontab

# Modern Celery settings (Lowercase configuration style for Celery 4.0+)
beat_schedule = {
    "cleanup-old-books": {
        "task": "worker.tasks.cleanup_old_books",
        "schedule": crontab(hour=2, minute=0),  # Daily at 2:00 AM
    },
    "reset-monthly-quotas": {
        "task": "worker.tasks.reset_monthly_quotas",
        "schedule": crontab(day_of_month=1, hour=0, minute=0),  # Monthly on the 1st at midnight
    },
}

task_routes = {
    "worker.tasks.process_pdf_task": {"queue": "pdf_processing"},
    "worker.tasks.cleanup_old_books": {"queue": "maintenance"},
    "worker.tasks.reset_monthly_quotas": {"queue": "maintenance"},
}
