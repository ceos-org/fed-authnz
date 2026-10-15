# Challenges and Strategic Solutions

This chapter identifies key challenges in implementing federated authentication and authorization systems and proposes solutions.

## Technical Complexities and Interoperability

## Attribute Management and Governance

## Policy, Legal and Compliance Considerations

### Data Protection, Transfer of Personal Data

#### Introduction
Federated authentication typically involves transfer of personal data stored in the user account at the IdP to the SP.
The Policy Enforcement Point (PEP) on the SP side checks the information transmitted from the IdP regarding authorization.

Therefore, data protection regulations apply to this cross-organizational transfer of personal data.
If both the IdP and the SP reside in the same jurisdiction, then the data protection regulation of this jurisdiction apply.

If the IdP and SP are located in different jurisdictions, then a legal basis for the cross-jurisdictional transfer of personal data must be found.

Depending on the specific use case and requirements, special sub-types of identity federations may be designed,
e.g. anonymous federations (the IdP sends information to the SP that is anonymous from the point of view of the SP)
or delegated authorization where (most of the) authorization checks are delegated from the SP to the IdP.


#### The General Data Protection Regulation of the European Union
The General Data Protection Regulation (GDPR) of the European Union (EU) defines a common data protection framework for the member states of the EU as well as entities worldwide that provide services inside the EU that involve the processing of personal data (Article 3 GDPR, territorial scope, https://gdpr-info.eu/art-3-gdpr/).

If personal data shall be transferred outside the territorial scope of the GDPR, additional GDPR requirements must be met that are laid down in Chapter 5 of the GDPR (https://gdpr-info.eu/art-44-gdpr/).
This applies to "third countries" as well as International Organisations (IO) such as ESA and EUMETSAT ("IO", Article 4 no. 26 GDPR).
The purpose is to ensure an adequate level of data protection using different instruments (Art. 45 ff GDPR), differing in effort and complexity, or at least to ensure an explicit consent of the data subject after having been informed about the possible risks.

Transferring personal data to partners outside the territorial scope of the GDPR is easiest if the European Commission has issued a so-called adequacy decision stating that data protection of the country/entity the data shall be transferred to is on a level adequate to the GDPR and therefore no further safeguards are required (Art. 46 GDPR). The current list of adequacy decisions can be found at https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en.

Thus, if an IdP residing in an EU country wants to transfer personal data to an SP residing outside the GDPR territory, this has to be taken into account.
Vice versa, if a SP residing in an EU country receives personal data from an international IdP, GDPR is fully applicable.


#### ESA Personal Data Protection Policy (PDP) Framework

As an International Organisation, ESA has defined a Personal Data Protection Policy (PDP) Framework composed of the following elements:
* The Principles of Personal Data Protection adopted by ESA Council on 13 June 2017
* The Rules of Procedure for the Data Protection Supervisory Authority adopted by ESA Council on 13 June 2017
* The Policy on Personal Data Protection (including its Annex “Governance Scheme of the Agency’s Personal Data Protection”) adopted by Director General of ESA on 1 March 2022. The duration of the Policy has been extended by Director General’s decision until 1 March 2028.

(online at https://esamultimedia.esa.int/docs/LEX-L/ESA_Principles_of_PDP_Rules_of_Procedure_for_DPSA_and_Policy.pdf).

(to be further filled by ESA, or removed if not enough content or not considered relevant enough)


#### International Transfer of Personal Data in eduGAIN

Exchanging account information and personal data between SPs and IdPs worldwide is at the heart of the international Meta-Federation eduGAIN and is by nature not limited to a single jurisdiction (as is the case of National Identity Federations).

Already before existence of the GDPR a "Code of Conduct" (CoCo) was developed for eduGAIN to address data protection best practices on an international level. Now being part of  REFEDS (Research and Education FEDerations group, https://refeds.org/), an updated version 2 has been published as "approach to meet the requirements of the EU GDPR in federated identity management. The Data protection Code of Conduct defines behavioral rules for Service Providers which want to receive user attributes from the Identity Providers managed by the Home Organisations. It is expected that Home Organisations are more willing to release attributes to Service Providers who manifest conformance to the Data protection Code of Conduct." (cited: https://wiki.refeds.org/display/CODE/Data+Protection+Code+of+Conduct+Home).

A number of documents, supporting materials and cookbooks for SPs, IdPs, Federation Operators and Home Organisations can be found here: https://wiki.refeds.org/display/CODE/Data+Protection+Code+of+Conduct+Home.




<mark>Note</mark> _[UR]_ this section would benefit from input from authors from other data protection jurisdictions / frameworks outside of GDPR


## Transformative Benefits for CEOS/EO Ecosystem
- **CEOS possible implementation**
