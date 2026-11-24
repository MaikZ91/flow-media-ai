# Instagram-Autopilot

Der Workflow veröffentlicht pro Lauf höchstens einen freigegebenen, fälligen Beitrag über Instagram API mit Instagram Login. Der Zeitplan prüft stündlich bei Minute 17. Uhrzeiten in der Warteschlange enthalten den jeweiligen UTC-Offset. Der Workflow berücksichtigt Beiträge bis zu 24 Stunden nach dem geplanten Zeitpunkt.

## Einrichten

1. In der Meta-App Instagram Login für das professionelle Instagram-Konto einrichten. Das Token braucht `instagram_business_basic` und `instagram_business_content_publish`.
2. In GitHub unter **Settings → Secrets and variables → Actions → Secrets** `IG_TOKEN`, `IG_USER_ID` und `IG_POST_QUEUE` hinterlegen. Als Repository-Variable `IG_API_VERSION` auf die API-Version der Meta-App setzen, inklusive `v`.
3. Einen freigegebenen Beitrag mit fertigen Medien in die JSON-Liste aufnehmen. Meta muss jedes Medium über die HTTPS-URL direkt abrufen können. Für Fotos und Bilderkarussells JPEG verwenden, für Reels MP4. Caption und Hashtags gehören in das gemeinsame Feld `caption`.

```json
[
  {
    "id": "mein-erster-beitrag",
    "approved": false,
    "publish_at": "2026-11-24T20:00:00+01:00",
    "format": "image",
    "media_urls": ["https://example.com/fertiges-bild.jpg"],
    "caption": "Text und Hashtags"
  }
]
```

Für `image` und `reel` genau eine URL angeben. Für `carousel` zwei bis zehn Bild-URLs angeben. Jede ID bleibt dauerhaft eindeutig. In diesem öffentlichen Repo für IDs neutrale Bezeichnungen ohne vertrauliche Angaben verwenden.

## Veröffentlichen

Nach dem Merge **Actions → Instagram Autopilot → Run workflow** auf `main` öffnen. Ohne gesetzte Option `publish` prüft der Workflow die Warteschlange. Mit gesetzter Option verarbeitet er den nächsten fälligen Eintrag. Sobald der erste Lauf geprüft ist, aktiviert die Repository-Variable `IG_AUTOPILOT_ENABLED=true` den Zeitplan. Zum Pausieren die Variable auf `false` setzen.

Beim ersten Veröffentlichungslauf legt der Workflow den Branch `instagram-autopilot-state` an. Dieser speichert Container- und Medien-IDs zur Vermeidung doppelter Beiträge. Bei einem unklaren Veröffentlichungsversuch hält der Workflow für den betroffenen Eintrag an. Vor jeder Wiederholung den Beitrag direkt auf Instagram und den Containerstatus prüfen.

Der Workflow liest vorbereitete Medien und die freigegebene Warteschlange. Die Erstellung von Beiträgen aus dem Postingplan, Rendering und Insights sind separate Schritte.
