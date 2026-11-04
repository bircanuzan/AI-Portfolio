# Oracle OTBI / Analytics Publisher / PMR executive reporting — proposed architecture

**INTERVIEW PORTFOLIO CASE — SYNTHETIC DATA. NOT A PRODUCTION ORACLE CONFIGURATION OR COMPANY-INTERNAL RESULT.**

## System of record
Oracle Fusion Cloud Talent Management (Performance Management, Goal Management, Talent Review, Succession Management, Career Development) plus authorised corporate LMS and finance sources. The HCM system of record is a **proposed enterprise architecture**, not independently verified as a particular employer's setup.

## Verified Oracle reporting technologies
- **Oracle Transactional Business Intelligence (OTBI)**: operational Talent KPI dashboard, performance documents, Goal Management status and alignment, talent-review meetings, successor candidates. Subject areas require release, security and tenant validation.
- **Oracle Analytics Publisher** (formerly BI Publisher, part of OTBI reporting stack): highly formatted report templates and data models with monthly / quarterly / annual PDF or Excel output, approved recipient schedules and security.
- **Oracle Fusion HCM Analytics** (Fusion Data Intelligence): separately licensed optional workforce trends, skills matrix, succession analysis and historical reports, with privacy and AI risk controls.
- **PMR executive scorecards**: operating and financial performance framework with signed narratives and board action register. Underlying corporate reporting software **not identified**.
- **Power BI**: optional external consolidation; not a default dependency of this Oracle-led project.

## Operational dashboard and subject-area catalogue

| Talent outcome | OTBI subject area | Management question |
|---|---|---|
| Review completion | Workforce Performance - Performance Document Status Real Time | Who owns 4-point gap to target? |
| Ratings distribution | Workforce Performance - Performance Rating Real Time | Was calibration completed fairly? |
| Goal alignment | Workforce Goals - Goal Alignments Real Time | Are goals linked to strategic objectives? |
| Goal progress | Workforce Goals - Goal Status Overview Real Time | What goals are stale or blocked? |
| Talent calibration | Workforce Talent Review - Talent Review Meeting Real Time | Which meetings are not final? |
| Succession | Workforce Succession Management - Plan Candidates Real Time | What critical positions have validated successors? |

Talent-review task subject areas and exact BI catalog names must be verified against the currently configured Oracle tenant; don't infer access or existence from a generic architecture.

## Analytics Publisher production delivery model
- Monthly: performance and goal exceptions. Audience: senior business leaders / HRBPs.
- Quarterly: successor readiness, strategic skills programme milestones, retention risk, overdue development actions. Audience: CHRO and executive committee.
- Annual: formal talent PMR scorecard with baseline, approved annual target, achieved performance, Finance-verified programme budget, commentary and decision/action record. Audience: board / committee through approved security channel.
- Build steps: authorised OTBI report or data model / HCM Extract → Analytics Publisher XML schema and RTF layout → test PDF/Excel → BI catalog security and scheduling → versioned signed board pack.
- This portfolio includes a synthetic XML example and a standalone formatted-report mockup, **not** a tenant-tested Publisher template.

## Data governance and executive trust
Validate as-of timestamp, review-cycle denominators, worker assignment status, unique critical positions, approved candidates, talent-review meeting finalisation, rating and nine-box row security, and suppress small cohorts. Reconcile financial investment to Finance/ERP, not HCM. Validate role permissions and automated recipient scheduling.

## Leadership value
This demonstrates annual talent operating plan ownership, performance governance, enterprise scorecard design, learning programme effectiveness, readiness risk management, executive narrative and evidence-gated approvals. It does not assert an installed platform, operational ROI, or live project hours.

### Official documentation
- https://docs.oracle.com/en/cloud/saas/analytics/26r3/fdioa/prebuilt-workbooks-related-subject-areas.html
- https://docs.oracle.com/en/cloud/saas/human-resources/24d/fahca/administering-analytics-and-reports-for-hcm.pdf
- https://docs.oracle.com/en/cloud/saas/human-resources/fahex/define-the-bi-publisher-template-in-hcm-extracts.html
- https://www.oracle.com/fusion-data-intelligence/hcm-analytics/
