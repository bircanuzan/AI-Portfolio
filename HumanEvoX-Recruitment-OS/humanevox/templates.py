"""Draft-only outreach, optional human-led conversation and calendar exports."""
from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4
from zoneinfo import ZoneInfo

STAGES = ("New", "Review", "Contacted", "Screen", "Client review", "Interview", "Offer", "Hired", "On hold", "Withdrawn")


def outreach_draft(name: str, role: str, company: str = "HumanEvoX Talent Consultancy", kind: str = "invitation") -> tuple[str, str]:
    first = name.strip().split(" ")[0] or "Candidate"
    if kind == "follow-up":
        return (f"Following up: {role}",
                f"Hello {first},\n\nI am following up regarding the {role} opportunity. "
                "Please let me know whether you would like to discuss the role and what times suit you.\n\n"
                f"Kind regards,\n{company}")
    if kind == "interview":
        return (f"Interview scheduling: {role}",
                f"Hello {first},\n\nWe would like to discuss the {role} opportunity. "
                "Could you share suitable time slots and your time zone? "
                "We will confirm details before sending an invitation.\n\n"
                f"Kind regards,\n{company}")
    return (f"Opportunity to discuss: {role}",
            f"Hello {first},\n\nI am reaching out from {company} regarding a {role} opportunity. "
            "Would you be open to reviewing the role details? We will share the opportunity "
            "and discuss next steps only if you are interested.\n\n"
            f"Kind regards,\n{company}")


def conversation_guide(role: str) -> str:
    return (f"Human-led screening guide — {role}\n\n"
            "1. Confirm interest and obtain permission to discuss the opportunity.\n"
            "2. Explain the position, organization (where authorised), location, and process.\n"
            "3. Ask for examples tied to the role's essential skills and note evidence.\n"
            "4. Ask about notice period, availability, and preferences only when relevant.\n"
            "5. Invite questions, explain how their information will be used and close.\n\n"
            "Capture factual notes. Do not record audio or start an AI call.")


def _ical_escape(s: str) -> str:
    return str(s).replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def invitation_ics(title: str, start: datetime, duration_minutes: int, description: str = "", location: str = "Microsoft Teams — to be confirmed") -> bytes:
    if start.tzinfo is None or start.utcoffset() is None:
        raise ValueError("Start time requires an explicit time zone")
    if not 15 <= duration_minutes <= 240:
        raise ValueError("Duration must be 15–240 minutes")
    from datetime import timedelta
    end = start + timedelta(minutes=duration_minutes)
    fmt = lambda d: d.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//HumanEvoX//Recruitment OS Pilot//EN", "BEGIN:VEVENT",
             f"UID:{uuid4()}@humanevox.com", f"DTSTAMP:{fmt(datetime.now(timezone.utc))}",
             f"DTSTART:{fmt(start)}", f"DTEND:{fmt(end)}", f"SUMMARY:{_ical_escape(title)}",
             f"DESCRIPTION:{_ical_escape(description)}", f"LOCATION:{_ical_escape(location)}",
             "STATUS:TENTATIVE", "END:VEVENT", "END:VCALENDAR"]
    return ("\r\n".join(lines) + "\r\n").encode("utf-8")
