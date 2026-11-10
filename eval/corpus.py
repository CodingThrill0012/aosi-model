"""Deterministic synthetic corpus of short internal-policy documents for the
DAIRM evaluation. The documents are generated from templates (no real policy
text); they exist only so that the Context Services plane has something to
retrieve."""
import random

TOPICS = ["password reset", "remote access", "data retention", "card dispute",
          "travel expenses", "laptop encryption", "vendor onboarding",
          "incident reporting", "privileged access", "customer complaints",
          "leave approval", "email phishing", "backup restore", "API keys",
          "mobile devices", "visitor access", "software installation",
          "cloud storage", "change management", "audit logging"]
ROLES = ["employees", "contractors", "branch staff", "IT administrators",
         "managers", "the security team", "auditors", "developers"]
ACTIONS = ["must be approved by", "must be reported to", "must be reviewed by",
           "must be logged and shared with", "requires written consent from"]
WINDOWS = ["within 24 hours", "within 3 working days", "every 90 days",
           "before the end of the quarter", "within 1 hour", "annually"]


def build(n_docs: int = 160, seed: int = 7):
    rnd = random.Random(seed)
    docs = []
    for i in range(n_docs):
        topic = TOPICS[i % len(TOPICS)]
        ver = 1 + i // len(TOPICS)
        sents = []
        for _ in range(5):
            sents.append(f"For {topic}, {rnd.choice(ROLES)} {rnd.choice(ACTIONS)} "
                         f"{rnd.choice(ROLES)} {rnd.choice(WINDOWS)}.")
        sents.append(f"This is policy section {i} on {topic}, version {ver}.")
        docs.append({"id": f"POL-{i:04d}", "topic": topic, "version": ver,
                     "text": " ".join(sents)})
    return docs


def questions(n: int, seed: int):
    rnd = random.Random(seed)
    tmpl = ["What is the rule for {t}?", "Who approves {t} requests?",
            "How quickly must {t} issues be reported?",
            "Summarise the policy on {t}."]
    return [rnd.choice(tmpl).format(t=rnd.choice(TOPICS)) for _ in range(n)]
