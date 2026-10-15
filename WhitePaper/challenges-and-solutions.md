# Challenges and Strategic Solutions

This chapter identifies key challenges in implementing federated authentication and authorization systems and proposes solutions.

## Technical Complexities and Interoperability

### Protocol Interoperability and Reusable IAM Integration
EO environments may combine services and identity infrastructures using different protocols and operational models. This includes the integration of OIDC-based services with research and education identity federations that predominantly use SAML.

Implementing federation functionality separately in each service would duplicate integration and maintenance effort. Protocol adaptation can instead be handled by a shared IAM component or identity broker, while connected services continue to use their existing authentication interfaces. Operation and security of the federation connection then become responsibilities of the operator of the shared component.

### Allocation of Federation Integration Responsibilities
Federation integration can be implemented at different architectural boundaries. The chosen boundary determines who operates, maintains, and configures the protocol adaptation.

The ongoing EOEPCA+ and DLR activities examine two approaches:

**Service-provider-side integration:** The EOEPCA+ IAM Building Block uses a SATOSA-based federation proxy within the Service Provider's IAM environment. Federation-specific configuration and integration with local IAM capabilities remain under the control of the service operator, who also operates and maintains the proxy component.

**Federation-provided integration:** The DLR EOC Geoservice uses an OIDC proxy provided by DFN-AAI. Parts of the federation-specific functionality are therefore operated by the federation provider, while the service uses an OIDC-facing integration.

[Figure X: Federation Integration Approaches for the EOEPCA+ IAM Building Block and DLR EOC Geoservice]

The figure illustrates these two integration scenarios, with particular emphasis on the location of protocol adaptation and the resulting operational responsibilities.

### Comparison of Federation Integration Approaches
Both approaches connect EO services to the existing federation infrastructure but differ in where federation-specific functionality is operated.

With EOEPCA+, the service operator controls federation configuration, attribute processing, and integration with the local IAM environment. This supports the role of the IAM Building Block as a reusable component serving multiple connected services, but also requires the operator to maintain the proxy and the necessary federation expertise.

In the DLR scenario, DFN-AAI operates the OIDC proxy and part of the federation-specific infrastructure. This reduces the functionality that has to be operated directly by the Service Provider, while making the integration dependent on the interfaces and services provided by the federation operator.

Both models can coexist within an EO environment. The integration boundary depends primarily on the protocols used by the service, the federation services available, and where responsibility for operating the federation connection should reside.

### Identity Provider Discovery and User Experience
An interfederation such as eduGAIN gives users access through a large number of institutional Identity Providers. EO services therefore need a practical way for users to locate and select their home organization.

A discovery service can support this selection step. Its integration also needs to account for the redirects between the EO service, federation components, and the institutional Identity Provider.

When multiple applications share a single IAM component, discovery can be implemented once at the IAM layer rather than separately in every application.

## Attribute Management and Governance
### Federated Identity Attributes and Local Authorization
Institutional Identity Providers supply identity attributes, but the available attributes can differ between institutions and may not contain the information required to authorize access to a particular dataset, processing service, or collaborative environment.

EO service operators need to define which attributes are required from the federation and how they are mapped to locally managed permissions and entitlements. Institutional affiliation alone, for example, is not sufficient to determine access to a restricted EO resource.

A shared IAM component can process federated identity information centrally, while connected services apply their own authorization policies to the resources they provide.

Cross-platform authorization and delegated access introduce additional requirements, especially when entitlements originate from another organization. These capabilities go beyond the authentication and federation functionality provided through eduGAIN.

### Identity Linking and Lifecycle Management
Using an institutional identity removes the need for an additional authentication credential, but EO services may still maintain local user profiles, permissions, or records of resource usage.

The federated identity must be linked reliably to the corresponding local user context. Stable identifiers and defined procedures are needed to handle changes such as a user's institutional affiliation, account status, or released identity attributes.

When several EO services share an IAM component, identity linking can be handled consistently at the IAM layer. Management and revocation of local permissions remain the responsibility of the respective EO environment.

Federation enables authentication through an external Identity Provider; it does not automatically synchronize the full lifecycle of local accounts and permissions.

## Policy, Legal and Compliance Considerations
### Federation Onboarding and Operational Governance
Connecting a service to an established identity federation involves organizational as well as technical work. 
Responsibilities have to be defined for service registration, metadata, security contacts, configuration, and ongoing operation.

Access to eduGAIN for a Service Provider is typically established through a participating national federation. 
The exact onboarding process and integration services available to Service Providers depend on the respective federation.

For the EOEPCA+ integration with DFN-AAI, current activities include organizational preparation, service registration, definition of the required attributes, and preparation for interfederation testing. 
Documenting these steps together with the technical configuration will provide a practical reference for similar EO integrations.

### Data Protection Considerations for Federated EO Services
Federated EO services receive identity information from external institutions and may involve organizations operating in different jurisdictions. 
Service operators need to identify which personal data is required for authentication, identity linking, and authorization, and how this data is processed and retained.

Identity brokers and protocol proxies add further components to the authentication flow and may also involve additional operators. 
Their respective roles and responsibilities need to be included when assessing the processing of identity information.

For a common IAM component serving several applications, attribute processing should be limited to the information required by the connected services and avoid unnecessary distribution of identity information.

Data protection requirements, including those concerning international data transfers, depend on the participating organizations, jurisdictions, and actual data flows. 
Documenting these flows and the corresponding operational responsibilities provides the basis for this assessment.

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
