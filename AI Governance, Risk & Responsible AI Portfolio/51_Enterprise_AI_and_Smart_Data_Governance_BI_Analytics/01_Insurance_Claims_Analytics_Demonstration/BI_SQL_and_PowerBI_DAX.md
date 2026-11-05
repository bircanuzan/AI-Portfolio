# BI semantic model & dashboard examples — NOT executed in a cloud BI environment

**Illustrative star schema:** FactClaims(claim_id, received_date_key, channel_key, amount_aed, missing_doc_count, review_score, suggested_route, final_human_status); DimDate(date_key, month, year); DimChannel(channel_key, channel); FactHumanOverride(claim_id, timestamp, reviewer_id_token, decision, reason_code); FactDataQuality(run_id, dataset, quality_pass, exceptions).

Do **not** derive insurer adjudication outcomes from the synthetic ground-truth label; it is only a toy generator target.

## SQL examples (illustrative dialect; not executed)
    SELECT submission_channel,
           COUNT(*) AS claims,
           SUM(CASE WHEN suggested_route = 'human_review' THEN 1 ELSE 0 END) AS review_suggestions,
           AVG(review_score) AS avg_review_score
      FROM synthetic_triage_output
     GROUP BY submission_channel
     ORDER BY submission_channel;

## Power BI / DAX measures (design examples; not tested in Power BI)
    Claims = COUNTROWS(FactClaims)
    Suggested Human Review = CALCULATE([Claims], FactClaims[suggested_route] = "human_review")
    Human Review Suggestion Rate = DIVIDE([Suggested Human Review], [Claims])
    Data Quality Pass Rate = DIVIDE(CALCULATE(COUNTROWS(FactDataQuality), FactDataQuality[quality_pass] = TRUE()), COUNTROWS(FactDataQuality))
    Human Override Rate = DIVIDE(COUNTROWS(FactHumanOverride), [Suggested Human Review])

## Proposed dashboard
- **Executive:** volume, workflow aging, manual review load, exceptional claims, quality threshold.
- **Operations:** by branch/channel; hold times; team backlog; human override reasons; error drill-through.
- **Risk:** missing data, drift alerts, subgroup QA, review overrides, incidents, unresolved control exceptions.
- **Controls:** row-level security per business role; sensitive data masking; aggregation thresholds; lineage; refresh SLA; accessible visual labels.

**Source-of-truth rules:** Define claim event timestamps, denominator for rates, late-arriving records, deduplication and data retention before publishing. Self-service BI is only approved after a certified semantic model and governed access.
