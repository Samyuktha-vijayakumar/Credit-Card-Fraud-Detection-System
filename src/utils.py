def risk_label(p):
    if p > 0.8:
        return "🔴 HIGH"
    elif p > 0.4:
        return "🟡 MEDIUM"
    else:
        return "🟢 LOW"


def decision(p):
    if p > 0.8:
        return "❌ Reject"
    elif p > 0.5:
        return "⚠ Review"
    else:
        return "✅ Approve"