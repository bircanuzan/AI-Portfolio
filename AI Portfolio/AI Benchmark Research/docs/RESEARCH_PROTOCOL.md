# Research & OSINT protocol

## 1. Define the answer before hunting for failures
Specify the target construct, domain, temporal cutoff, response format, tool permissions, and what a correct answer means. Separate the researcher's evidence hunt from the model's later test. Record a task ID and version. Do not design a riddle with multiple equally plausible answers.

## 2. Hard-fact discovery (public sources only)
Start with an indirect clue rather than a direct answer search. Expand through official registries, government filings, patent metadata, standards bodies, institutional archives, academic repositories, regional-language/local records, historical scans, and archived superseded documents. Record:
- Initial and refined search queries, including negative results and language variations;
- The discovery chain: clue → document identifier → official record → answer;
- Source publisher, publication date, exact URL, access date, and relevant page/section;
- Why an ordinary direct search is insufficient, and any contamination risk.

**No scraping behind access controls, de-anonymization of private people, or unauthorized access.** Follow site terms and privacy requirements.

## 3. Primary-source verification
Prioritize the issuing authority's official record over blogs and AI summaries. When independent primary sources exist, seek two; when one authoritative issuing source is the only primary source, add a separate corroboration note instead of inventing independence. Cross-check dates, author names, versions and units. Capture contradictions and explain which record controls.

A **source ledger** must distinguish (a) confirms the answer, (b) supports an intermediate clue, (c) contradicts, and (d) only repeats a secondary claim. Capture permanent IDs, canonical URLs, access date, content excerpt or section, and any material corrections or errata.

## 4. Answer-key freeze
Write one unambiguous final question with a short canonical answer. Document permitted formatting aliases (not semantic alternatives), answer type, evidence URLs, reasoning bridge, exclusion of tempting distractors, and a stability note. Never copy a benchmark's hidden/held-out answers into this public repository.

## 5. Adversarial task design
Generate candidate traps: wrong-year documents, similarly named standards, obsolete numbers, surface-search false positives, cross-lingual naming variants, source citation without source support, and instructions embedded in retrieved text. Confirm the challenge tests research strategy, not a misleading prompt.

## 6. Pilot and calibration
Use a controlled set of available model versions with exact settings, browsing enabled/disabled state, retry policy, tool budgets and evaluation date recorded. Collect final answer, authorized search/tool logs and citation URLs. Do **not** claim to inspect private reasoning chains. Label each attempt as correct / incorrect / not attempted. A synthetic replay is not a live test.

## 7. Ambiguity and reviewer gate
A task is **rejected** if two competent independent reviewers derive different supported answers, if evidence is inaccessible, if answer is unstable without a cutoff, or if wording leaks the answer. Ask reviewers to reconstruct the solution *without* the author's private notes. Escalate contested items for adjudication, retain review history, and remove or revise defective tasks.

## 8. Re-use and scaling
Turn a validated failure mechanism into new candidates across independent domains. De-duplicate entities, source URLs and reasoning paths; avoid changing only the surface story. Keep a held-out set for future evaluations and monitor data leakage. Version any change to question, key or sources. Publish uncertainty rather than overclaim.

## Example source ledger (verified baseline fixtures)
| Task | Ground truth | Issuer / record | Evidence |
|---|---|---|---|
| BMR-001 | 600-1 | NIST GenAI Profile, published 2024-07-26 | [Official record](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) |
| BMR-002 | 300 | Meta GAIA publication summary (2024-05-06) | [Official research page](https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants/) |
| BMR-003 | 1,266 | OpenAI BrowseComp article (2025-04-10) | [Official article](https://openai.com/index/browsecomp/) |
| BMR-004 | RFC 9110 | RFC Editor HTTP Semantics record (June 2022) | [Official RFC](https://www.rfc-editor.org/info/rfc9110/) |

**Limit:** these four examples exercise an auditable authoring/grading workflow. Their difficulty against current models is **not established**. More difficult archive-based items require separate research logs, independent verification and live tests before promotion.