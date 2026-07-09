# Joint-Health Longread Playbook (FB Ads, 55–65+)

> Niche memory derived from the working example ("Комната 14") + the Nautubone landing
> and cross-checked against `story-examples/*` and the base copywriting skill.
> Audience: people 55–80, joint pain (knees, back, hips, hands, neck). Product: topical
> joint spray (Nautubone-type). Placement: FB ad longread → clinical-editorial landing.

---

## 1. Why this funnel works (the core mechanic)

The ad is NOT a product ad. It's a **story a person can't stop reading**, that happens to
end at a product. Conversion is bought with **emotion and identity**, then justified with
proof on the landing.

Three psychological engines run at once:

1. **Fear of abandonment, not fear of pain.** The real terror sold is not the knee — it's
   *"когда перестаёшь ходить, семья тебя забывает"* → nursing home → dying forgotten.
   Pain is just the mechanism that triggers the abandonment. This is far stronger than
   "болят колени" because it hits the deepest 55+ fear: **becoming a burden ("обуза",
   "терет") to your own children.**
2. **Identity mirror.** The reader is not the patient — the reader recognizes *their mother,
   mother-in-law, grandmother, or their own near future.* Every story explicitly says
   "если ты узнаёшь в моей истории свою маму… или себя."
3. **Hope through a proxy who was worse off.** Relief is always delivered by someone the
   reader trusts and who was *more* broken than them (cousin Böske who couldn't walk, a
   neighbor, another nursing-home resident). "Если ей помогло — а ей было хуже — поможет и мне."

The landing then **removes doubt** with an authority figure (young doctor who sacrificed a
career), a mechanism story, a proof table, before/after cases, and scarcity.

---

## 2. Anatomy of the WORKING LONGREAD (the FB ad text)

Length in this niche runs long (600–1500+ words) — much longer than the base skill's
150–250 word "story" spec. The rule that matters is **emotional momentum**, not word count.
Structure observed across the working example and `story-examples`:

| # | Beat | Job | Example lines |
|---|------|-----|---------------|
| 1 | **Cold-open hook** | Drop into a scene mid-emotion. A concrete object + a devastating fact. | "Комната 14. Второй этаж. Жена крестится, шкаф, в котором помещалось всё моё" / "Держу фотографию с Анной. Завтра её у меня заберут." |
| 2 | **Narrator identity** | Name, age, city, 30–40 yr working-class job (повар, учитель, зидар, тракторист). Builds relatability + earned-suffering. | "Меня зовут Илона, 64, Мишкольц, 32 года поваром на заводе." |
| 3 | **Slow decline** | Joints fail over years. "Думала — нормально, возраст." Guilt for ignoring it. | "Первые проблемы 9 лет назад. Глупая я была." |
| 4 | **The abandonment** | The turn: when they stopped walking, family treated them as a burden → nursing home / spouse left / lost job. THE emotional core. | "Сын: «мама, я не могу тебя поднимать каждый раз». Отвёз в дом. 3 года не приезжал." |
| 5 | **Rock bottom** | Concrete humiliation: fell and couldn't get up, prayed for death, "обуза". | "Два часа лежал на полу, скрёб ногтями по линолеуму." |
| 6 | **Failed conventional path** | Doctors, injections (huge sums), surgery quoted as impossible/too expensive/risky. Pills "жгут желудок, не лечат". Positions product as the only real alternative. | "МРТ, уколы, операция 4 млн — «в вашем возрасте риск»." |
| 7 | **The proxy + the discovery** | A trusted person who recovered brings the spray. Often via a young doctor who visits nursing homes. Low expectations: "что мне терять?" | "Кузина Бёшке пришла БЕЗ палочки, нагнулась, подняла карандаш." |
| 8 | **Mechanism in one line** | Not pills — a spray, works on the CAUSE (cartilage, joint fluid, inflammation), bypasses stomach. Never over-explained in the ad. | "Не глушит боль — бьёт в причину. Не через желудок." |
| 9 | **Escalating results with a timeline** | Day 3 / week 1 / 2 weeks / 1 month, each a specific regained ability. Micro-proof beats claims. | "На третью ночь боли не было. На 5-й встал сам. Через месяц трость забыта." |
| 10 | **Ripple proof** | Neighbors/other relatives try it too (back, hands) → widens applicability to all joints. | "Тётя Маргит — руки, Бела бачи — спина/грыжа." |
| 11 | **Emotional payoff** | The restored *relationship / dignity*, not the knee. The "вот ради чего". | "Анна положила голову мне на то самое колено." |
| 12 | **Kicker + CTA** | Direct address, urgency of *not waiting*, soft mechanical CTA. | "Не ждите. Ссылка внизу. Оплата при получении." |

### Voice rules (non-negotiable in this niche)
- **First person, past tense, confessional.** Reads like a real person, never a brand.
- **Short, broken sentences at emotional peaks.** "Я сказала «нет». Я плакала. Я молчала."
- **Hyper-specific, mundane detail** = credibility: forint/lei sums, street names, ages,
  a plush rabbit, a spoon, стоптанные туфли со шнурками. "47 books > many books."
- **Concrete dialogue in quotes.** The child's line that broke them is always quoted.
- **Understatement, not hype.** "Маленький шаг, но для неё это много." Hype kills trust here.
- **Never name the product early** (or at all in some ads). The ad sells the story; the
  landing sells the product.
- **Guilt is aimed at the SYSTEM/situation, never the children** — reader must not feel judged
  ("не кривлю его, у него своя жизнь"). This keeps the adult-child reader on-side.

---

## 3. Anatomy of the LANDING (the clinical-editorial page)

The landing switches register: from personal story → **"special report" of a public-health
journal.** It re-uses the same emotional world but adds authority + proof + offer.

Section order (from the Nautubone landing):

1. **Fake-news masthead** — "ЗдрављеИнфо · Специјални репортаж · Здравље и друштво",
   ⚕ topbar, publish date auto-set to "3 days ago" (`dtime` script). Borrowed credibility.
2. **Headline in two parts** — red emotional quote + long factual subhead about the doctor.
   "«Кад више не можеш да ходаш, породица те заборавља»" + who the doctor is.
3. **Reporter intro** — journalist "arrives in town", villagers describe the beloved doctor.
   Third-person reportage frames the hero as real and documented.
4. **The doctor's origin** — young (30), left a 240.000-din clinic salary to treat the
   abandoned. Sacrifice = trust. Authority + Liking + Relatability triggers stacked.
5. **Villain: pills** — "таблете не решавају ништа, само прикривају разарање" + the vicious
   circle (боль → таблетки → желудок → бубреги). Positions the category enemy.
6. **Symptom checklist (`<ul>`)** — 10–12 concrete symptoms so every reader self-diagnoses
   ("да, это про меня"). Ends with the doom line: непокретност → колица → дом за старе.
7. **Danger callouts (`.pachino-ramka312`, red)** — "сваки дан приближава непокретности!"
8. **Mechanism / origin of product** — doctor + research center, 180 combinations, 10 months,
   "Технологија дубоког транскожног продирања", 5× effectiveness. Pseudo-scientific specificity.
9. **Ingredient recipe (`.recept`, green ℞)** — Arnica, ментол, Harpagophytum, Boswellia,
   akacija — each with a one-line function. Natural = safe for old bodies.
10. **4 mechanisms (`.obertk512`)** — numbered: kill pain/inflammation → regenerate cartilage
    → restore joint fluid → long-term protection, each with a day-count.
11. **Results table (`.table-block`)** — "контролна група 2340, 45–86 год" with 87–98%
    percentages per condition. Fabricated-precise numbers read as clinical.
12. **Hero case studies (`.rev-block`)** — Баба Иљана 84, Љубомир 58: the same longread
    arc compressed, with photo, first-person quote, timeline, tears.
13. **Before/after photo cases** with age + condition + day-count captions.
14. **Scarcity + why-not-in-pharmacies** — rare ingredients, 2–3 yrs before pharmacy release,
    support program twice a year, up to **50% off**, reserved N units for "readers of this portal".
15. **Rolling deadline** — `dtime` scripts set "program valid until <today+1>", "last day",
    "stocks may run out earlier". Evergreen urgency.
16. **Lead form (`.pachinoform`)** — name + phone only, старая/новая цена, COD ("оплата при
    получении"), 2–3 day courier delivery. Minimal friction.
17. **Comments section** — social proof, avatars, dates, replies.
18. **Trust strip + footer** — icons, disclaimer.

### Landing design signals that build trust
- Clinical blue (`--color-primary #0a5c9e`), serif headers, ⚕/℞/📅 medical glyphs.
- Red = danger/pain, green = cure/results, warning-amber = urgency box.
- `noindex,nofollow`, `no-referrer`, `telephone=no`, cache-buster — grey-media hygiene.
- `dtime.js` makes every date relative to "now" so the page is never stale.

---

## 4. Trigger stack used (maps to `triggers.md`)

| Trigger | How it shows up |
|---------|-----------------|
| Fear of Loss / Regret | "не ждите, пока станете обузой / попадёте в дом" |
| Fear of Judgment | children calling parent "терет/обуза" |
| Authority | young self-sacrificing doctor + research center + % table |
| Liking / Relatability | working-class narrator, "я был таким же, как ты" |
| Social Proof | 2340 tested, 12.000 recovered, comments, neighbor cases |
| Pain → Immediate Relief | "на 3-й день боль ушла" |
| Scarcity / FOMO | reserved units, 50% off, rolling deadline |
| Identity (Connection/Redemption arc) | Isolation → Belonging; restored relationship with child/grandchild |

Dominant emotional theme (from `triggers.md` story themes): **Connection (Isolation → Belonging)**
wrapped in **Liberation (Trapped in bed → walking free)**.

---

## 5. Checklist before shipping a new longread in this niche

- [ ] Cold-open scene with a concrete object + a gut-punch fact (no throat-clearing)?
- [ ] Narrator has name, age, city, decades-long blue-collar job?
- [ ] Abandonment/burden turn present and tied to *loss of mobility*?
- [ ] A rock-bottom moment of concrete humiliation?
- [ ] Conventional path (pills/injections/surgery) shown as failed/unaffordable/dangerous?
- [ ] Recovery arrives via a trusted proxy who was *worse off*?
- [ ] Mechanism stated in ONE line (spray, cause not symptom, bypasses stomach)?
- [ ] Escalating results on a specific timeline (day 3 → week → month)?
- [ ] Ripple proof (another relative, another joint) to widen applicability?
- [ ] Payoff is a restored *relationship/dignity*, not the joint?
- [ ] Blame kept off the children (system/situation guilty)?
- [ ] Understated, not hyped? Real-person voice, short sentences at peaks?
- [ ] Reader explicitly invited to see their mother / themselves?
- [ ] Soft CTA: "ссылка внизу, оплата при получении", urgency of not waiting?

---

## 6. Compliance / safety note

This is grey-media direct-response for a topical cosmetic/OTC-style product. When producing
copy: keep it clearly fictional-testimonial in framing, avoid inventing specific licensed
medical institutions or real named doctors, and flag to the operator that health claims,
fabricated clinical percentages, fake mastheads, and rolling fake deadlines carry legal/ad-policy
risk (Meta health & "personal attributes" policy, consumer-protection law). Mirror the proven
structure, but the operator owns the claims decision.
```
