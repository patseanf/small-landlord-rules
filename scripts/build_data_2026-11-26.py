# One-off generator for launch data (2026-11-26). Every rule/fee below was read from the cited official URL on this date.
import json, os
D = os.path.join(os.path.dirname(__file__), "..", "data")
C = "2026-11-26"

CA_DEP="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1950.5"
CA_ENT="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954"
CA_TER="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.1"
TX92="https://statutes.capitol.texas.gov/Docs/PR/htm/PR.92.htm"
TX91="https://statutes.capitol.texas.gov/Docs/PR/htm/PR.91.htm"
FL49="http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0083/Sections/0083.49.html"
FL53="http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0083/Sections/0083.53.html"
FL57="http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0083/Sections/0083.57.html"
NYAG="https://ag.ny.gov/sites/default/files/tenants_rights.pdf"
WA=lambda c: f"https://app.leg.wa.gov/RCW/default.aspx?cite={c}"
AZ=lambda n: f"https://www.azleg.gov/ars/33/{n}.htm"
MA15B="https://malegislature.gov/Laws/GeneralLaws/PartII/TitleI/Chapter186/Section15B"
MA12="https://malegislature.gov/Laws/GeneralLaws/PartII/TitleI/Chapter186/Section12"
VA=lambda s: f"https://law.lis.virginia.gov/vacode/title55.1/chapter12/section{s}/"
OH=lambda s: f"https://codes.ohio.gov/ohio-revised-code/section-{s}"
NC=lambda s: f"https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_42/GS_{s}.html"
MI=lambda s: f"https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-{s}"

TOPICS = {
 "deposit-cap": "Security deposit limit",
 "deposit-return": "Security deposit return deadline",
 "late-fee": "Late fee rules",
 "entry-notice": "Landlord entry notice",
 "termination-notice": "Ending a month-to-month tenancy",
}

def R(topic, answer, detail, quote, citation, url, source_name, title=None):
    return dict(topic=topic, title=title or TOPICS[topic], answer=answer, detail=detail, quote=quote,
                citation=citation, sourceUrl=url, sourceName=source_name, checkedAt=C)

STATES = [
 ("CA","California","california",[
  R("deposit-cap","1 month's rent (2 months for qualifying small landlords)",
    "A landlord may not take security above one month's rent, on top of first month's rent. A landlord who is a natural person (or an LLC whose members are all natural persons) and owns no more than two rental properties with no more than four units in total may take up to two months' rent. The two-month exception does not apply when the prospective tenant is a service member.",
    "a landlord shall not demand or receive security, however denominated, in an amount or value in excess of an amount equal to one month’s rent, in addition to any rent for the first month paid on or before initial occupancy.",
    "Cal. Civ. Code § 1950.5(c)", CA_DEP, "California Legislative Information"),
  R("deposit-return","21 calendar days after the tenant moves out",
    "Within 21 calendar days after the tenant has vacated, the landlord must send an itemized statement of deductions and return the rest of the deposit.",
    "No later than 21 calendar days after the tenant has vacated the premises ... the landlord shall furnish the tenant, a copy of an itemized statement indicating the basis for, and the amount of, any security received and the disposition of the security, and shall return any remaining portion of the security to the tenant",
    "Cal. Civ. Code § 1950.5(h)(1)", CA_DEP, "California Legislative Information"),
  R("entry-notice","Reasonable written notice; 24 hours is presumed reasonable",
    "Outside emergencies, the landlord must give reasonable written notice and enter during normal business hours. The notice must give the date, approximate time and purpose. Mailed notice sent at least six days ahead is presumed reasonable.",
    "Twenty-four hours shall be presumed to be reasonable notice in absence of evidence to the contrary.",
    "Cal. Civ. Code § 1954(d)(1)", CA_ENT, "California Legislative Information"),
  R("termination-notice","Owner: 60 days (30 days if the tenant has lived there under 1 year)",
    "An owner ending a periodic residential tenancy under this section must give at least 60 days' written notice, or 30 days if the tenant has lived there less than one year. A tenant must give notice at least as long as the rent period. Other California laws, including just-cause eviction rules, may also apply.",
    "An owner of a residential dwelling ... giving notice pursuant to this section shall give notice at least 60 days prior to the proposed date of termination. A tenant giving notice pursuant to this section shall give notice for a period at least as long as the term of the periodic tenancy prior to the proposed date of termination.",
    "Cal. Civ. Code § 1946.1(b)–(c)", CA_TER, "California Legislative Information"),
 ]),
 ("TX","Texas","texas",[
  R("deposit-return","On or before the 30th day after the tenant surrenders the unit",
    "The landlord must refund the security deposit (less lawful deductions) by the 30th day after the tenant surrenders the premises.",
    "the landlord shall refund a security deposit to the tenant on or before the 30th day after the date the tenant surrenders the premises.",
    "Tex. Prop. Code § 92.103(a)", TX92+"#92.103", "Texas Constitution and Statutes"),
  R("late-fee","Only after rent is unpaid 2 full days; up to 12% (≤4 units) or 10% (>4 units) is presumed reasonable",
    "A late fee requires notice in a written lease, must be reasonable, and can only be charged once rent has stayed unpaid two full days after the due date. A fee of no more than 12% of the month's rent (buildings with four or fewer units) or 10% (more than four units) is considered reasonable.",
    "any portion of the tenant's rent has remained unpaid two full days after the date the rent was originally due.",
    "Tex. Prop. Code § 92.019", TX92+"#92.019", "Texas Constitution and Statutes"),
  R("termination-notice","At least one month (tenancy ends the later of the notice date or one month after notice)",
    "Either side may end a month-to-month tenancy by notice. When the rent period is at least a month, the tenancy ends on the later of the date in the notice or one month after the notice is given, unless the parties agree otherwise in writing.",
    "the tenancy terminates on whichever of the following days is the later: (1) the day given in the notice for termination; or (2) one month after the day on which the notice is given.",
    "Tex. Prop. Code § 91.001(b)", TX91+"#91.001", "Texas Constitution and Statutes"),
 ]),
 ("FL","Florida","florida",[
  R("deposit-return","15 days if no claim; 30 days to send notice of a claim",
    "If the landlord is not claiming any of the deposit, it must be returned within 15 days after the lease ends. To claim part of it, the landlord must send written notice of the claim within 30 days, by certified mail or e-mail as allowed by s. 83.505. Missing the 30-day notice forfeits the right to take the claim out of the deposit.",
    "the landlord must return the security deposit, together with interest if otherwise required, within 15 days after the termination of the rental agreement. If the landlord intends to impose a claim on the deposit, the landlord must, within 30 days after the termination of the rental agreement, provide the tenant written notice",
    "Fla. Stat. § 83.49(3)(a)", FL49, "The Florida Senate / Online Sunshine"),
  R("entry-notice","24 hours' notice for repairs, between 7:30 a.m. and 8:00 p.m.",
    "For repairs, reasonable notice means at least 24 hours, and a reasonable time is between 7:30 a.m. and 8:00 p.m. A landlord may enter at any time to protect or preserve the premises.",
    "“Reasonable notice” for the purpose of repair is notice given at least 24 hours prior to the entry, and reasonable time for the purpose of repair shall be between the hours of 7:30 a.m. and 8:00 p.m.",
    "Fla. Stat. § 83.53(2)", FL53, "The Florida Senate / Online Sunshine"),
  R("termination-notice","Not less than 30 days before the end of a monthly period",
    "Either party may end a month-to-month tenancy with written notice of not less than 30 days before the end of any monthly period.",
    "When the tenancy is from month to month, by giving not less than 30 days’ notice prior to the end of any monthly period",
    "Fla. Stat. § 83.57(3)", FL57, "The Florida Senate / Online Sunshine"),
 ]),
 ("NY","New York","new-york",[
  R("deposit-cap","No more than 1 month's rent",
    "A security deposit is limited to one month's rent. The New York Attorney General notes this means a landlord cannot ask for last month's rent and a security deposit.",
    "all tenants can be required to give their landlord a security deposit, but it is limited to no more than one month’s rent.",
    "NY Attorney General, Residential Tenant’s Rights Guide (Security Deposits)", NYAG, "New York State Attorney General"),
  R("deposit-return","Within 14 days of move-out (non-regulated units)",
    "For units that are not rent stabilized or rent controlled, the deposit must be returned within 14 days of move-out, with an itemized statement for any deductions. Without that statement in 14 days, the whole deposit must be returned.",
    "the landlord must return the security deposit within 14 days of the tenant moving out.",
    "NY Attorney General, Residential Tenant’s Rights Guide (Getting Your Security Deposit Back)", NYAG, "New York State Attorney General"),
  R("late-fee","Late only after 5 days; max is the lesser of $50 or 5% of monthly rent",
    "Rent counts as late only if it arrives more than five days after it is due, and the late fee can be no more than $50 or 5% of the monthly rent, whichever is less.",
    "A rent payment can only be considered late if it is received more than five days after it is due. The most your landlord can charge as a late fee is $50 or 5% of your monthly rent, whichever is less (Real Property Law § 238-a).",
    "N.Y. Real Prop. Law § 238-a (per NY AG guide)", NYAG, "New York State Attorney General"),
  R("termination-notice","Non-renewal or 5%+ increase: 30, 60 or 90 days' notice depending on tenure",
    "Before not renewing a lease or raising rent more than 5%, a landlord must give 30 days' notice (under 1 year), 60 days (1–2 years) or 90 days (2+ years or a 2-year lease).",
    "If you have lived in your apartment for less than one year, or have a lease for less than one year, your landlord must provide you with 30 days advanced notice before raising your rent or not renewing your lease. (Real Property Law § 226-c).",
    "N.Y. Real Prop. Law § 226-c (per NY AG guide)", NYAG, "New York State Attorney General", title="Non-renewal and rent increase notice"),
 ]),
 ("WA","Washington","washington",[
  R("deposit-return","Within 30 days after the tenancy ends and the tenant vacates",
    "Within 30 days, the landlord must give a full and specific statement of the basis for keeping any of the deposit, with required documentation, plus any refund due.",
    "Within 30 days after the termination of the rental agreement and vacation of the premises ... the landlord shall give a full and specific statement of the basis for retaining any of the deposit",
    "RCW 59.18.280(1)(a)", WA("59.18.280"), "Washington State Legislature"),
  R("entry-notice","At least 2 days' written notice",
    "Outside emergencies, the landlord must give at least two days' written notice stating the date and time (or time window) of entry, and enter only at reasonable times.",
    "the landlord shall give the tenant at least two days' written notice of his or her intent to enter and shall enter only at reasonable times.",
    "RCW 59.18.150", WA("59.18.150"), "Washington State Legislature"),
  R("late-fee","No late fee if rent is paid within 5 days of the due date",
    "A landlord cannot charge a late fee for rent paid within five days after it is due. After that, late fees may run from the first day after the due date.",
    "The landlord may not charge a late fee for rent that is paid within five days following its due date.",
    "RCW 59.18.170(2)", WA("59.18.170"), "Washington State Legislature"),
  R("termination-notice","Tenant: 20 days' written notice before the end of a rental period",
    "A month-to-month tenant ends the tenancy with written notice of 20 days or more before the end of a rental period. Landlord-initiated terminations are governed by other sections of RCW 59.18 and are not summarized here.",
    "such tenancy ... shall end by written notice of 20 days or more, preceding the end of any of the months or periods of tenancy, given by the tenant to the landlord.",
    "RCW 59.18.200(1)(a)", WA("59.18.200"), "Washington State Legislature", title="Tenant notice to end a month-to-month tenancy"),
 ]),
 ("AZ","Arizona","arizona",[
  R("deposit-cap","1.5 months' rent (including prepaid rent)",
    "Total security, including prepaid rent, cannot exceed one and one-half months' rent. A tenant may still voluntarily prepay more rent.",
    "A landlord shall not demand or receive security, however denominated, including prepaid rent in an amount or value of more than one and one-half month's rent.",
    "A.R.S. § 33-1321(A)", AZ("01321"), "Arizona State Legislature"),
  R("deposit-return","14 days (excluding weekends and legal holidays) after move-out and the tenant's demand",
    "After the tenancy ends, possession is delivered and the tenant asks, the landlord has 14 business days to send an itemized list of deductions and any amount owed.",
    "Within fourteen days, excluding Saturdays, Sundays or other legal holidays, after termination of the tenancy and delivery of possession and demand by the tenant the landlord shall provide the tenant an itemized list of all deductions together with the amount due",
    "A.R.S. § 33-1321(D)", AZ("01321"), "Arizona State Legislature"),
  R("entry-notice","At least 2 days' notice",
    "Except in emergencies or where impracticable, the landlord must give at least two days' notice and enter only at reasonable times.",
    "the landlord shall give the tenant at least two days' notice of the landlord’s intent to enter and enter only at reasonable times.",
    "A.R.S. § 33-1343(D)", AZ("01343"), "Arizona State Legislature"),
  R("late-fee","Must be reasonable and set out in a written rental agreement (no dollar cap in this section)",
    "The statute refers to a reasonable late fee set forth in a written rental agreement. Section 33-1368 does not set a dollar or percentage cap.",
    "the rental agreement shall be reinstated if the tenant tenders all past due and unpaid periodic rent and a reasonable late fee set forth in a written rental agreement.",
    "A.R.S. § 33-1368(B)", AZ("01368"), "Arizona State Legislature"),
  R("termination-notice","30 days' written notice before the periodic rental date",
    "Either the landlord or tenant may end a month-to-month tenancy with written notice at least 30 days before the rental date named in the notice.",
    "The landlord or the tenant may terminate a month-to-month tenancy by a written notice given to the other at least thirty days prior to the periodic rental date specified in the notice.",
    "A.R.S. § 33-1375(B)", AZ("01375"), "Arizona State Legislature"),
 ]),
 ("MA","Massachusetts","massachusetts",[
  R("deposit-cap","1 month's rent (the first month's rent amount)",
    "At the start of a tenancy a landlord may collect no more than first month's rent, last month's rent and a security deposit equal to the first month's rent (plus a lock-and-key cost), subject to the statute's conditions.",
    "a security deposit equal to the first month's rent provided that such security deposit is deposited as required by subsection (3) and that the tenant is given the statement of condition as required by subsection (2)",
    "Mass. Gen. Laws ch. 186, § 15B(1)(b)", MA15B, "The 194th General Court of Massachusetts"),
  R("deposit-return","Within 30 days after the tenancy ends",
    "The landlord must return the deposit, or the balance after lawful deductions, within 30 days after the tenancy ends.",
    "The lessor shall, within thirty days after the termination of occupancy under a tenancy-at-will or the end of the tenancy as specified in a valid written lease agreement, return to the tenant the security deposit or any balance thereof",
    "Mass. Gen. Laws ch. 186, § 15B(4)", MA15B, "The 194th General Court of Massachusetts"),
  R("late-fee","No interest or penalty until rent is 30 days late",
    "A lease cannot impose interest or a penalty for late rent until 30 days after the rent was due.",
    "No lease or other rental agreement shall impose any interest or penalty for failure to pay rent until thirty days after such rent shall have been due.",
    "Mass. Gen. Laws ch. 186, § 15B(1)(c)", MA15B, "The 194th General Court of Massachusetts"),
  R("termination-notice","Rent interval or 30 days, whichever is longer",
    "A tenancy at will with monthly rent ends with written notice equal to the interval between rent days or 30 days, whichever is longer.",
    "the time of such notice shall be sufficient if it is equal to the interval between the days of payment or thirty days, whichever is longer.",
    "Mass. Gen. Laws ch. 186, § 12", MA12, "The 194th General Court of Massachusetts", title="Ending a tenancy at will"),
 ]),
 ("VA","Virginia","virginia",[
  R("deposit-cap","2 months' rent",
    "A landlord may not demand or receive a security deposit above two months' periodic rent.",
    "No landlord may demand or receive a security deposit, however denominated, in an amount or value in excess of two months' periodic rent.",
    "Va. Code § 55.1-1226(A)", VA("55.1-1226"), "Code of Virginia (Virginia Law Library)"),
  R("deposit-return","Within 45 days after the tenancy ends or the tenant vacates (whichever is later)",
    "Deductions must be itemized in a written notice given with any amount due within 45 days.",
    "The security deposit and any deductions, damages, and charges shall be itemized by the landlord in a written notice given to the tenant, together with any amount due to the tenant, within 45 days after the termination date of the tenancy or the date the tenant vacates the dwelling unit, whichever occurs last.",
    "Va. Code § 55.1-1226", VA("55.1-1226"), "Code of Virginia (Virginia Law Library)"),
  R("late-fee","Must be in the written lease; max is the lesser of 10% of rent or 10% of the balance due",
    "A late charge must be in the written rental agreement and cannot exceed the lesser of 10% of the periodic rent or 10% of the remaining balance owed.",
    "No such late charge shall exceed the lesser of 10 percent of the periodic rent or 10 percent of the remaining balance due and owed by the tenant.",
    "Va. Code § 55.1-1204(E)", VA("55.1-1204"), "Code of Virginia (Virginia Law Library)"),
  R("entry-notice","72 hours' notice for routine maintenance the tenant didn't request",
    "Landlords must give notice and enter at reasonable times; for routine maintenance not requested by the tenant, at least 72 hours' notice is required, and the work must happen within 14 days.",
    "Unless impractical to do so, the landlord shall give the tenant at least 72 hours' notice of routine maintenance to be performed that has not been requested by the tenant.",
    "Va. Code § 55.1-1229", VA("55.1-1229"), "Code of Virginia (Virginia Law Library)"),
  R("termination-notice","30 days' written notice before the next rent due date (unless the lease says otherwise)",
    "Either party may end a month-to-month tenancy with written notice at least 30 days before the next rent due date, unless the rental agreement sets a different period.",
    "The landlord or the tenant may terminate a month-to-month tenancy by serving a written notice on the other at least 30 days prior to the next rent due date, unless the rental agreement provides for a different notice period.",
    "Va. Code § 55.1-1253(A)", VA("55.1-1253"), "Code of Virginia (Virginia Law Library)"),
 ]),
 ("OH","Ohio","ohio",[
  R("deposit-return","Within 30 days after the lease ends and possession is delivered",
    "Itemized deductions and any refund are due within 30 days. The tenant must give the landlord a forwarding address in writing.",
    "Any deduction from the security deposit shall be itemized and identified by the landlord in a written notice delivered to the tenant together with the amount due, within thirty days after termination of the rental agreement and delivery of possession.",
    "Ohio Rev. Code § 5321.16(B)", OH("5321.16"), "Ohio Laws (Legislative Service Commission)"),
  R("entry-notice","Reasonable notice; 24 hours is presumed reasonable",
    "Except in emergencies or where impracticable, the landlord must give reasonable notice and enter at reasonable times. 24 hours is presumed reasonable.",
    "Twenty-four hours is presumed to be a reasonable notice in the absence of evidence to the contrary.",
    "Ohio Rev. Code § 5321.04(A)(8)", OH("5321.04"), "Ohio Laws (Legislative Service Commission)"),
  R("termination-notice","30 days before the periodic rental date",
    "Either side may end or not renew a month-to-month tenancy with notice at least 30 days before the periodic rental date.",
    "the landlord or the tenant may terminate or fail to renew a month-to-month tenancy by notice given the other at least thirty days prior to the periodic rental date.",
    "Ohio Rev. Code § 5321.17(B)", OH("5321.17"), "Ohio Laws (Legislative Service Commission)"),
 ]),
 ("NC","North Carolina","north-carolina",[
  R("deposit-cap","1.5 months' rent for month-to-month; 2 months for longer terms; 2 weeks for week-to-week",
    "The cap depends on the tenancy: two weeks' rent (week-to-week), one and one-half months' rent (month-to-month), two months' rent (terms longer than month-to-month).",
    "The security deposit shall not exceed an amount equal to two weeks' rent if a tenancy is week to week, one and one-half months' rent if a tenancy is month to month, and two months' rent for terms greater than month to month.",
    "N.C. Gen. Stat. § 42-51(b)", NC("42-51"), "North Carolina General Assembly"),
  R("deposit-return","Within 30 days (interim accounting allowed; final within 60 days)",
    "The landlord must itemize damage and return the balance within 30 days after the tenancy ends. If the claim can't be determined in 30 days, an interim accounting is due in 30 days and a final one within 60.",
    "no later than 30 days after termination of the tenancy and delivery of possession of the premises to the landlord.",
    "N.C. Gen. Stat. § 42-52", NC("42-52"), "North Carolina General Assembly"),
  R("late-fee","Only after 5 days late; monthly rent: the greater of $15 or 5%",
    "A late fee may be charged only when rent is five calendar days or more late. For monthly rent, the cap is $15 or 5% of the monthly rent, whichever is greater.",
    "If the rent: (1) Is due in monthly installments, a landlord may charge a late fee not to exceed fifteen dollars ($15.00) or five percent (5%) of the monthly rent, whichever is greater.",
    "N.C. Gen. Stat. § 42-46(a)", NC("42-46"), "North Carolina General Assembly"),
  R("termination-notice","7 days' notice for month-to-month",
    "A month-to-month tenancy ends with seven days' notice; week-to-week with two days; year-to-year with one month.",
    "a tenancy from month to month by a like notice of seven days; a tenancy from week to week, of two days.",
    "N.C. Gen. Stat. § 42-14", NC("42-14"), "North Carolina General Assembly"),
 ]),
 ("MI","Michigan","michigan",[
  R("deposit-cap","1.5 months' rent",
    "A security deposit may not exceed one and one-half months' rent.",
    "A security deposit shall be required and maintained in accordance with the terms of this act and shall not exceed 1 1/2 months' rent.",
    "MCL 554.602", MI("554-602"), "Michigan Legislature"),
  R("deposit-return","Itemized notice of damages within 30 days after occupancy ends",
    "To keep any of the deposit for damage, the landlord must mail an itemized notice of damages within 30 days after the tenant's occupancy ends.",
    "the landlord shall mail to the tenant, within 30 days after the termination of occupancy, a notice of damages that contains an itemized list of damages claimed",
    "MCL 554.609(1)", MI("554-609"), "Michigan Legislature", title="Security deposit damage notice deadline"),
  R("termination-notice","1 month's notice (or the rent interval, if rent is paid more often)",
    "A tenancy at will may be ended by either party with one month's notice. If rent is payable at periods of less than three months, notice equal to the interval between payments is sufficient.",
    "an estate at will or by sufferance may be terminated by either party by giving 1 month's notice to the other party.",
    "MCL 554.134(1)", MI("554-134"), "Michigan Legislature", title="Ending a tenancy at will"),
 ]),
]

ALL_STATES = [("AL","Alabama"),("AK","Alaska"),("AZ","Arizona"),("AR","Arkansas"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),("DE","Delaware"),("DC","District of Columbia"),("FL","Florida"),("GA","Georgia"),("HI","Hawaii"),("ID","Idaho"),("IL","Illinois"),("IN","Indiana"),("IA","Iowa"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("ME","Maine"),("MD","Maryland"),("MA","Massachusetts"),("MI","Michigan"),("MN","Minnesota"),("MS","Mississippi"),("MO","Missouri"),("MT","Montana"),("NE","Nebraska"),("NV","Nevada"),("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NY","New York"),("NC","North Carolina"),("ND","North Dakota"),("OH","Ohio"),("OK","Oklahoma"),("OR","Oregon"),("PA","Pennsylvania"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VT","Vermont"),("VA","Virginia"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming")]
slugify=lambda n: n.lower().replace(" ","-").replace(".","")
verified={code:(name,slug,rules) for code,name,slug,rules in STATES}
out=[]
for code,name in ALL_STATES:
    if code in verified:
        n,slug,rules=verified[code]
        for r in rules: r["slug"]=f"{slug}-{r['topic']}"
        missing=[t for t in TOPICS if t not in {r['topic'] for r in rules}]
        out.append(dict(code=code,name=n,slug=slug,status="verified",checkedAt=C,rules=rules,pendingTopics=missing))
    else:
        out.append(dict(code=code,name=name,slug=slugify(name),status="queued",checkedAt=None,rules=[],pendingTopics=list(TOPICS)))
json.dump(dict(topics=TOPICS,states=out),open(f"{D}/states.json","w"),indent=2,ensure_ascii=False)

# ---------------- tools ----------------
def T(slug,name,category,site,pricingUrl,plans,screening,ach,card,notes,sources,bestFor):
    return dict(slug=slug,name=name,category=category,website=site,pricingUrl=pricingUrl,plans=plans,screening=screening,ach=ach,card=card,notes=notes,sources=sources,bestFor=bestFor,checkedAt=C)
P=lambda n,p,note=None: dict(name=n,price=p,note=note)
CHK="Check provider"
tools=[
 T("turbotenant","TurboTenant","All-in-one landlord software","https://www.turbotenant.com/","https://www.turbotenant.com/pricing/",
   [P("Free","$0/month"),P("Essentials","From $12.42/month","$149/year for 1–10 units"),P("Pro","From $16.58/month","$199/year for 1–10 units")],
   "Renter-paid: $55 on the free plan, $45 on Pro","$2 on the free plan; free on Pro","3.49%",
   ["Landlords can choose to pay the screening fee themselves.","Standalone tenant placement (Autopilot) is a one-time $1,500 flat fee."],
   [{"label":"TurboTenant pricing","url":"https://www.turbotenant.com/pricing/"}],"Landlords who want free listings, applications and screening with an optional annual upgrade"),
 T("rentredi","RentRedi","All-in-one landlord software","https://rentredi.com/","https://rentredi.com/pricing",
   [P("Monthly","$29.95/month"),P("6-month","$20/month","billed semi-annually"),P("Annual","$12/month","billed annually")],
   "Tenant-paid: $39.99 (credit, criminal, eviction) or $49.99 with income verification",CHK,CHK,["Credit reporting is $5.99/month, landlord- or tenant-paid.","Every plan includes the full feature set and unlimited properties, tenants and teammates.","30-day money-back guarantee; no contract."],
   [{"label":"RentRedi pricing","url":"https://rentredi.com/pricing"}],"Landlords who want one flat subscription with unlimited units"),
 T("avail","Avail","All-in-one landlord software","https://www.avail.com/","https://www.avail.com/pricing",
   [P("Unlimited","$0/unit"),P("Unlimited Plus","$9/unit/month")],
   "Varies by location (state law); tenant-paid by default, landlord can cover. "+CHK,"$2.50 per bank transfer on the free plan (tenant-paid); $0 on Unlimited Plus","3.5% (tenant-paid, any plan)",
   ["Unlimited Plus adds FastPay, waived ACH charges and custom application questions."],
   [{"label":"Avail pricing","url":"https://www.avail.com/pricing"}],"Small landlords who want state-specific leases and free core tools"),
 T("innago","Innago","All-in-one landlord software","https://innago.com/","https://innago.com/faq/",
   [P("Free","$0/month","no setup fee or contract")],
   "$30–$35 per applicant (applicant-paid); +$10 for income verification","$2 per ACH payment (tenant-paid by default; landlord can choose to absorb)","2.99%",
   ["Innago states it is 100% free for landlords and earns from tenant transaction and screening fees."],
   [{"label":"Innago FAQ (pricing)","url":"https://innago.com/faq/"}],"Landlords who want a fully free platform and are fine with tenant-paid fees"),
 T("baselane","Baselane","Banking + bookkeeping + rent collection","https://www.baselane.com/","https://www.baselane.com/pricing",
   [P("Core","$0/month"),P("Smart","$20/month","on an annual plan; 30-day trial")],
   "From $24.99","$2–$5 per ACH rent payment (waived for Baselane deposits); landlord can cover or pass on","3.49% (debit or credit)",
   ["Checkbooks $15; mailed checks $2; outbound domestic wires $15 (waived at $50,000+ combined balance).","Banking is provided by Thread Bank, Member FDIC."],
   [{"label":"Baselane pricing","url":"https://www.baselane.com/pricing"}],"Landlords who want rental banking and bookkeeping in one place"),
 T("stessa","Stessa","Bookkeeping + rent collection","https://www.stessa.com/","https://www.stessa.com/pricing/",
   [P("Essentials","Free"),P("Manage","$12/month","paid annually ($15 monthly)"),P("Pro","$28/month","paid annually ($35 monthly)")],
   "Via RentPrep: $29 credit only, $29 background only, $49 complete package","Check provider","Check provider",
   ["Manage adds a Schedule E report, legal forms and accelerated rent payments."],
   [{"label":"Stessa pricing","url":"https://www.stessa.com/pricing/"},{"label":"Stessa help: screening reports","url":"https://support.stessa.com/en/articles/13273570-screening-reports-explained"}],"Investors focused on bookkeeping and tax-time reports"),
 T("rentec-direct","Rentec Direct","Property management software","https://www.rentecdirect.com/","https://www.rentecdirect.com/pricing.php",
   [P("Starter","$25/month","up to 10 properties"),P("Pro","From $50/month"),P("PM","From $50/month","adds trust accounting and owner portal")],
   "Starter $14.95–$29.45; Pro/PM $10.00–$18.00","Starter $2.00; Pro/PM: 1 free incoming ACH per active property per month, then $0.50","Starter 3.50%; Pro/PM 2.95% (Amex 3.50%)",
   ["Two-week free trial; no setup fees or contracts.","Cash payments via PayNearMe on Pro/PM ($200 setup; $4.99 tenant-paid per payment)."],
   [{"label":"Rentec Direct pricing","url":"https://www.rentecdirect.com/pricing.php"}],"Landlords who want published, all-in pricing and US-based support"),
 T("doorloop","DoorLoop","Property management software","https://www.doorloop.com/","https://www.doorloop.com/pricing",
   [P("DoorLoop One","From $2.50/unit/month","billed yearly; minimum spend and units apply"),P("DoorLoop Connect","From $4.00/unit/month","minimum spend and units apply")],
   "$35","Incoming ACH from $1.50; free incoming ACH on Connect","Check provider",
   ["As low as $1.50 per unit above 100 units on One."],
   [{"label":"DoorLoop pricing","url":"https://www.doorloop.com/pricing"}],"Growing portfolios that want full accounting and AI tenant messaging"),
 T("buildium","Buildium","Property management software","https://www.buildium.com/","https://www.buildium.com/pricing/",
   [P("Essential","From $65/month"),P("Growth","From $202/month"),P("Premium","From $420/month")],
   "$17 per screening (landlord-paid), or $35 applicant-paid; enhanced $20 (Growth & Premium)","Incoming EFT $2.35 (Essential), $1.35 (Growth), free 12 months then $0.60 (Premium)","2.99%",
   ["Bank account setup fee: $99 per business bank account on Essential."],
   [{"label":"Buildium pricing","url":"https://www.buildium.com/pricing/"}],"Property managers and larger portfolios"),
 T("hemlane","Hemlane","Software + leasing services","https://www.hemlane.com/","https://www.hemlane.com/pricing/",
   [P("Starter","$0/month"),P("Basic","$2/unit + $28 platform fee","$30/month for one unit"),P("Essential","$20/unit + $28 platform fee","$48/month for one unit; adds a repair coordinator")],
   "$40 total, tenant-paid","No fee on paid plans","3%",
   ["Optional listing syndication to 7 exclusive websites is $89 for 30 days."],
   [{"label":"Hemlane pricing","url":"https://www.hemlane.com/pricing/"}],"Remote landlords who want repair coordination"),
 T("zillow-rental-manager","Zillow Rental Manager","Listings + applications","https://www.zillow.com/rental-manager/","https://www.zillow.help/article/paying-for-your-zillow-rental-manager-listings-zd30237393777555",
   [P("Listing","Free"),P("Premium listing","$39.99 per listing","up to 90 days; no auto-renew")],
   "Free for landlords; renters pay $40 (reusable for 30 days)","Check provider","Check provider",
   ["Free and premium listings include online screening and rent payments."],
   [{"label":"Zillow help: paying for listings","url":"https://www.zillow.help/article/paying-for-your-zillow-rental-manager-listings-zd30237393777555"},{"label":"Zillow Rental Manager tenant screening","url":"https://www.zillow.com/rental-manager/tenant-screening/"}],"Landlords who mainly need listing reach plus free applications"),
 T("apartments-com-rental-manager","Apartments.com Rental Manager","Listings + applications","https://www.apartments.com/rental-manager/","https://propertyhelp.apartments.com/article/13-applicant-cost",
   [P("Applications & screening","Free for landlords")],
   "Applicants pay $32.00 + tax (shareable with up to 10 landlords for 30 days)","Check provider","Check provider",
   ["Screening reports are from TransUnion."],
   [{"label":"Apartments.com help: applicant cost","url":"https://propertyhelp.apartments.com/article/13-applicant-cost"}],"Landlords listing on Apartments.com who want free applications"),
 T("rentprep","RentPrep","Tenant screening","https://rentprep.com/","https://rentprep.com/guide/packages-pricing/",
   [P("Credit Report Only","$29 per applicant"),P("Full Background Check Only","$29 per applicant","landlord-pay only"),P("Complete Screening Package","$49 per applicant")],
   "$29–$49 per applicant; add-ons $10 (income) or $15 (income + employment)","Not applicable","Not applicable",
   ["RentPrep reports are now delivered by Stessa. Landlord- and tenant-pay options exist for the credit and complete packages; background-only is landlord-pay."],
   [{"label":"RentPrep packages & pricing","url":"https://rentprep.com/guide/packages-pricing/"}],"Landlords who only need screening"),
 T("transunion-smartmove","TransUnion SmartMove","Tenant screening","https://www.mysmartmove.com/","https://www.mysmartmove.com/pricing",
   [P("Membership","Free","pay per report")],
   "Pay-per-report packages (SmartCheck Premium, Plus, Basic); landlord or applicant can pay. Package prices: "+CHK,"Not applicable","Not applicable",
   ["No memberships, subscriptions or minimums."],
   [{"label":"SmartMove pricing","url":"https://www.mysmartmove.com/pricing"}],"Landlords who want TransUnion reports without software"),
 T("steadily","Steadily","Landlord insurance","https://www.steadily.com/","https://www.steadily.com/",
   [P("Landlord policy","Quote-based")],
   "Not applicable","Not applicable","Not applicable",
   ["Steadily does not publish fixed prices; premiums come from an online quote."],
   [{"label":"Steadily","url":"https://www.steadily.com/"}],"Landlords shopping for rental property insurance"),
]
json.dump(dict(checkedAt=C,tools=tools),open(f"{D}/tools.json","w"),indent=2,ensure_ascii=False)

aff=[
 dict(tool="turbotenant",program="TurboTenant Affiliate Program",signupUrl="https://www.turbotenant.com/affiliates/",network="Impact",commission="$40 per customer + $5 per lead",contact="partners@turbotenant.com",termsUrl="https://www.turbotenant.com/affiliates/",termsVerified=True),
 dict(tool="rentredi",program="RentRedi Partner Program",signupUrl="https://rentredi.com/affiliate-program",network="Impact",commission="20% per qualified subscription; 30-day cookie",contact="partners@rentredi.com",termsUrl="https://rentredi.com/affiliate-program",termsVerified=True),
 dict(tool="baselane",program="Baselane Affiliate Program",signupUrl="https://www.baselane.com/partner-with-us",network="Not stated",commission="Up to $150 per qualified referral (page header says up to $200)",contact=None,termsUrl="https://www.baselane.com/partner-with-us",termsVerified=True),
 dict(tool="rentec-direct",program="Rentec Direct Affiliate Program",signupUrl="https://www.rentecdirect.com/blog/announcing-the-upgraded-rentec-direct-affiliate-program/",network="In-house (electronic affiliate agreement)",commission="25% of sales for 12 months + $10 per free-trial signup (announced Mar 2023)",contact="info@rentecdirect.com",termsUrl="https://www.rentecdirect.com/blog/announcing-the-upgraded-rentec-direct-affiliate-program/",termsVerified=True),
 dict(tool="innago",program="Innago Affiliate Program",signupUrl="https://innago.com/affiliate-program/",network="Not stated",commission="Check program page",contact=None,termsUrl="https://innago.com/affiliate-program/",termsVerified=False),
 dict(tool="avail",program="Avail Affiliate Partner Program",signupUrl="https://info.avail.com/affiliate-program",network="Not stated",commission="Not published",contact=None,termsUrl="https://info.avail.com/affiliate-program",termsVerified=False),
 dict(tool="steadily",program="Steadily Partners",signupUrl="https://www.steadily.com/partners",network="Awin (merchant 42963)",commission="Awin listing shows $20 per lead (not on Steadily's own page)",contact=None,termsUrl="https://ui.awin.com/merchant-profile/42963",termsVerified=False),
]
links=[]
for t in tools:
    a=next((x for x in aff if x["tool"]==t["slug"]),None)
    links.append(dict(tool=t["slug"],name=t["name"],url=t["website"],affiliateUrl=None,affiliateStatus="pending" if a else "no-program-known",program=a))
json.dump(dict(note="Links point to official sites until Patrick is approved; then set affiliateUrl and affiliateStatus='active'.",checkedAt=C,links=links),open(f"{D}/affiliates.json","w"),indent=2,ensure_ascii=False)

comps=[
 dict(slug="turbotenant-vs-avail",a="turbotenant",b="avail",title="TurboTenant vs Avail: fees compared",
  summary="Both have a $0 tier. TurboTenant's paid tier is a flat annual price; Avail's paid tier is per unit. Avail's free plan charges tenants $2.50 per bank transfer vs TurboTenant's $2 on its free plan.",
  points=["Paid tier: TurboTenant Pro is $199/year for 1–10 units; Avail Unlimited Plus is $9/unit/month.","Bank transfers: TurboTenant free plan $2, Pro free; Avail free plan $2.50 (tenant-paid), Unlimited Plus $0.","Cards: TurboTenant 3.49%; Avail 3.5%.","Screening: TurboTenant $55 (free) / $45 (Pro), renter-paid; Avail varies by location."]),
 dict(slug="baselane-vs-stessa",a="baselane",b="stessa",title="Baselane vs Stessa: fees compared",
  summary="Both start free and both bank through Thread Bank. Baselane's paid tier is $20/month (annual); Stessa's paid tiers are $12 and $28/month (annual).",
  points=["Paid tiers: Baselane Smart $20/month on an annual plan; Stessa Manage $12/month and Pro $28/month (annual).","Screening: Baselane from $24.99; Stessa via RentPrep $29–$49.","ACH rent: Baselane $2–$5 (waived for Baselane deposits); Stessa: check provider."]),
 dict(slug="rentredi-vs-innago",a="rentredi",b="innago",title="RentRedi vs Innago: fees compared",
  summary="Innago is free for landlords and earns from tenant fees. RentRedi charges the landlord a subscription ($12/month billed annually up to $29.95 month-to-month).",
  points=["Landlord cost: RentRedi $12–$29.95/month depending on billing term; Innago $0.","Tenant ACH: Innago $2 (tenant-paid); RentRedi: check provider.","Screening: Innago $30–$35 applicant-paid by default; RentRedi $39.99 tenant-paid ($49.99 with income verification)."]),
]
for c in comps: c["checkedAt"]=C
json.dump(dict(comparisons=comps),open(f"{D}/comparisons.json","w"),indent=2,ensure_ascii=False)

# ---------------- nightly queue ----------------
q=[]
def add(kind,title,slug,hint,prio):
    q.append(dict(id=f"{kind}:{slug}",type=kind,title=title,targetSlug=slug,sourceHint=hint,priority=prio,status="queued"))
big=["IL","PA","GA","NJ","CO","TN","IN","MO","MD","WI","MN","OR","SC","AL","LA","KY","OK","CT","UT","NV","IA","AR","MS","KS","NM","NE","ID","WV","HI","NH","ME","MT","RI","DE","SD","ND","AK","DC","VT","WY"]
nm=dict(ALL_STATES)
for i,code in enumerate(big):
    add("state-rules",f"{nm[code]} landlord rules: deposit limit, return deadline, late fees, entry and notice",slugify(nm[code]),"Official state legislature code site or state AG/housing agency only",1 if i<10 else 2)
for st in out:
    if st["status"]=="verified":
        for t in st["pendingTopics"]:
            add("rule",f"{st['name']}: {TOPICS[t]}",f"{st['slug']}-{t}","Official statute text; if the statute is silent, cite an official source that says so",2)
for name in ["TenantCloud","Landlord Studio","RentSpree","AppFolio","Rentler","SimplifyEm","Tellus","Azibo","RentDrop","Landlordy"]:
    add("tool",f"{name}: real fees for small landlords",slugify(name),"Provider's own pricing/fee pages only",2)
for a,b in [("turbotenant","rentredi"),("turbotenant","innago"),("avail","innago"),("baselane","turbotenant"),("rentec-direct","buildium"),("doorloop","buildium"),("hemlane","turbotenant"),("rentprep","transunion-smartmove"),("zillow-rental-manager","apartments-com-rental-manager"),("stessa","rentredi"),("avail","rentredi"),("doorloop","rentec-direct")]:
    add("compare",f"{a} vs {b}: fees compared",f"{a}-vs-{b}","Both providers' pricing pages, re-checked the same night",2)
for slug,title in [("chicago-rlto","Chicago Residential Landlord and Tenant Ordinance (RLTO)"),("new-york-city","New York City local rules for landlords"),("seattle","Seattle local landlord-tenant rules"),("san-francisco","San Francisco rent ordinance basics"),("los-angeles","Los Angeles rent stabilization (RSO) basics"),("washington-dc","Washington, DC landlord-tenant rules"),("portland-or","Portland, OR local rental rules"),("minneapolis","Minneapolis tenant protections"),("philadelphia","Philadelphia landlord rules"),("denver","Denver rental licensing and rules")]:
    add("city",title,slug,"City/county code or official housing department page",3)
json.dump(dict(rules="Publish at most 2 items per night. Re-fetch the official source the same night; if a number can't be verified from an official source, skip the item and log it. Never guess.",updatedAt=C,items=q),open(f"{D}/nightly-queue.json","w"),indent=2,ensure_ascii=False)

ch=[dict(date=C,type="launch",title="Launch: 11 states (42 statute-cited rules), 15 tools, 3 comparisons",paths=["/states","/tools"])]
json.dump(dict(entries=ch),open(f"{D}/changelog.json","w"),indent=2,ensure_ascii=False)
print("states verified",sum(1 for s in out if s["status"]=="verified"),"rules",sum(len(s["rules"]) for s in out),"tools",len(tools),"queue",len(q))
