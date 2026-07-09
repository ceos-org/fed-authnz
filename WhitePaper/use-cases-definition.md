# Use Cases Definition

This chapter defines the specific use cases for federated authentication and authorization in Earth Observation systems.


## ESA/NASA MAAP

### Motivation and Scope

The ESA–NASA Multi‑Mission Algorithm and Analysis Platform (MAAP) is a jointly developed initiative comprising two independently operated but interoperable cloud‑based platforms. While operated under separate organizational governance, the ESA and NASA MAAPs share a common architectural vision, interoperability standards, and mission objectives, supporting missions such as BIOMASS, NISAR, and GEDI.

### User‑Centric Goals of MAAP Federation

*\[SMB\] The MAAP federation architecture is evolving; the level of technical detail presented here focuses on conceptual goals and intended capabilities rather than a finalized operational architecture.*

The goal of federation between the ESA and NASA MAAP platforms is to reduce friction for cross‑platform scientific workflows while preserving platform autonomy. Practically, this means (1) accepting authentication performed by a user's home Identity Provider (IdP) and (2) enforcing authorization locally at the hosting MAAP, potentially using entitlement/attribute information that originates from the user's home side. This avoids a centralised identity or access‑control service while still enabling controlled access to protected resources.

### Value‑Adding Cross‑Platform Use Cases

The use cases below are included only to motivate authn/authz requirements (federated identity recognition, entitlement‑aware authorization, and auditability). They are not intended as a complete MAAP feature overview.

#### Federated Data Discovery and Access

Federated access enables users to discover and retrieve datasets hosted on either MAAP platform. Users search across distributed catalogues, access protected datasets, and retrieve data regardless of which organization hosts the underlying repository.

This reduces the need for multiple accounts and divergent access procedures when data is distributed across agency platforms.

#### Cross‑Platform Processing and Analysis

The joint MAAP architecture enables users to deploy and execute processing workflows across both platforms. From a user's notebook or analysis environment, a processor can be run against datasets hosted on different MAAPs with minimal platform‑specific changes (for example, endpoint selection and required credentials).

This approach supports execution of the same processor across different datasets and enables users to retrieve and compare the outputs from both platforms to validate consistency.

### Federation as the Enabling Mechanism

The cross‑platform use cases above rely on an established federation that allows the hosting MAAP to accept authentication performed by the user's home IdP and to bind it to a local session. The hosting MAAP then makes authorization decisions under local governance, potentially using entitlement information originating from the home side.

"Federation" refers to the trust relationships and interfaces needed for (a) acceptance of home authentication assertions and (b) exchange of authorization inputs (for example, entitlements).

#### Federation Use Case: Bilateral Delegated Authentication and Entitlement Propagation

This use case instantiates the pattern ("authenticate at home, authorize locally") for BIOMASS: the home organization authenticates the user and is authoritative for certain entitlements, while the hosting MAAP enforces authorization and auditing under local governance.

##### Context

The BIOMASS mission benefits from close collaboration between ESA and NASA partner infrastructures. A user may request BIOMASS resources hosted by either organization while authenticating with their home IdP.

Entitlements relevant to BIOMASS access are authoritative at the user's
home side and are made available to the hosting MAAP through a federated mechanism.

Authorization is enforced by the hosting MAAP and may incorporate entitlement information obtained from the home side; authentication assertions alone are not assumed to be sufficient for authorization.

##### Actors

- End User
- Home Identity Provider
- Partner Identity Provider
- Peer platforms operated by ESA and NASA
    - Home BIOMASS MAAP
    - Hosting BIOMASS MAAP

##### Preconditions

- The user holds an account at their home organization (ESA EOIAM or NASA EDL).
- The user has been granted the BIOMASS initiative entitlement at their home organization.
- A bilateral trust relationship exists between ESA EOIAM and NASA EDL.
- Federated entitlement exchange between peered MAAPs has been established.

##### Main Flow

1. The user requests access to a protected BIOMASS resource hosted by the partner MAAP.
2. The hosting MAAP redirects the user to authenticate with their home IdP.
3. The home IdP authenticates the user and returns an authentication assertion to the hosting side.
4. The hosting side validates the assertion and establishes a local session bound to a stable federated user identifier.
5. The hosting MAAP retrieves (or validates) the user's BIOMASS entitlement from the authoritative home side via a trusted platform‑to‑platform interface.
6. The hosting MAAP evaluates local authorization policy using the authenticated identity and retrieved entitlement information.
7. If authorized, the user is granted access under the hosting MAAP's controls (including auditing), regardless of which organization hosts the resource.

*Note:* On first use, deployments commonly require explicit user consent
for attribute release on the home side and acceptance of terms and
conditions on the hosting side; exact handling is policy‑driven.

##### Postconditions

- Access control is enforced by the hosting MAAP under local policy.
- The user can obtain the credentials/tokens required by that MAAP deployment to use permitted services.
- The user performs actions supported by the MAAP according to their entitlement.

Depending on local policy, this can avoid separate manual user
registration or account provisioning at the partner organization.

##### Key Properties

- Bilateral federation with mutual recognition of identities.
- Cross‑organization entitlement propagation.
- Explicit user consent and legal acceptance at first use.
- Operational equivalence between local and federated users.

```{mermaid}
sequenceDiagram
    title BIOMASS MAAP – Bilateral Delegated Authentication and Authorization Flow

    actor User
    box "Home organization"
        participant HomeIdP as Home IdP
        participant MAAP as Home BIOMASS MAAP
    end
    box "Partner organization"
        participant PartnerIdP as Partner IdP
        participant P_MAAP as Hosting BIOMASS MAAP
    end

    Note over MAAP,P_MAAP: Either MAAP may be operated by ESA or NASA.<br/>Roles are determined per access request.

    User->>P_MAAP: Access Hosting BIOMASS MAAP
    P_MAAP->>User: Redirect to authenticate

    User->>HomeIdP: Authenticate
    HomeIdP-->>User: Authentication successful

    alt First federation use
        HomeIdP->>User: Request consent for attribute sharing
        User-->>HomeIdP: Consent granted
        PartnerIdP->>User: Present Terms & Conditions
        User-->>PartnerIdP: Accept T&Cs
    end

    HomeIdP->>PartnerIdP: Assert identity (user identifier)

    PartnerIdP->>PartnerIdP: Validate assertion
    PartnerIdP->>PartnerIdP: Map to local security context

    User->>P_MAAP: Access Hosting MAAP environment

    P_MAAP->>MAAP: Query entitlement state (federated user identifier)
    MAAP-->>P_MAAP: Entitlement information

    P_MAAP-->>User: Access granted according to entitlement
```

### Extensions and Background

#### Platform‑to‑Platform Federation (API‑Level)

Beyond interactive user access, the ESA and NASA MAAP platforms may also establish service‑to‑service trust to support backend workflows (for example, orchestration and entitlement validation). *\[FWI\] This is included as context only; protocol choices and implementation specifics are intentionally out of scope for this chapter.*

[NASA MAAP](https://maap-project.org/)

[ESA MAAP (BIOMASS)](https://portal.maap.eo.esa.int/biomass/)

```{image} img/esa-nasa-maap-earthdata-1.png
:alt: ESA MAAP
:width: 90%
:class: image-spaced
```

```{image} img/esa-nasa-maap-earthdata-2.png
:alt: NASA MAAP
:width: 90%
:class: image-spaced
```

[NASA MAAP](https://maap-project.org/)

[ESA MAAP (BIOMASS)](https://portal.maap.eo.esa.int/biomass/)

## NASA Use Case (TBC) 

## DestinE (TBC)
DestinE has two federated solutions in place: 
1. Federated Identity Provider: A federated IdP generates client credentials which are passed to the DESP Admin. They configure client credentials and specific settings. The DESP login panel then shows the added IdP IAM. Federated IdPs can login into the DestinE platform without needing to create a DESP account. 
2. Federated Services: Similiar to the federated IdP, federated services generate client credentials which are passed to the Fed. Service Admin who configures client credentials and specific settings. These are then passed to the federated service login panel which shows the DESP IAM as an IdP. Examples of these services are SesamEO and other data access services of the platform like Eden, DCMS, HDA, etc. A dedicated DestinE-IAM Documentation is provided to SPs when performing the onboarding.

[DestinE Platform Onboarding Policy and Process v2.6](https://platform.destine.eu/wp-content/uploads/2024/11/DEST-SRCO-PR-2300339-Onboarding-Policy-and-Process-v2.6.pdf)

## Bilateral ESA-DLR Demonstrator
The bilateral ESA-DLR Demonstrator activity focuses on use cases regarding _Federated Discovery_ and _Federated Access_:
- _Federated Discovery_ refers to the ability to search for and discover data across several repositories hosted by different organizations in a unified way;
- _Federated Access_ refers to the ability to retrieve data using the digital identity (credentials) of the home organization no matter what organization participating in the identity federation is hosting the data.

The aim is to showcase the benefits of federating ressources on the data, service and identity level.

To support the use cases described below, and due to the character as a technical demonstration, free and open datasets (without restricting licences) are used to serve as examples for both free and open as well as restricted data. For user accounts virtual user identities are used.
For real world federated discovery / federated access applications, legal, data protection, licence and IT security aspects must be considered which have been excluded in this Demonstrator activity.

The following use cases (UC) are considered:
- UC1: A user can access a client and discover _free and open_ data from online repositories hosted by different organizations and can download a granule from the data set.
- UC2: A user can access a client and discover _restrained_ data from online repositories hosted by different organizations and can authenticate with the digital identity of the home organization in order to download a granule from a restrained data set.
- UC3: A user can access a client and discover data (_free and open_ or _restrained_) data located in near-line/offline repositories (archived data) hosted by different organizations and can download a granule (deferred access).
- UC4: A data manager can access a client and obtain information about data hosted in online, near-line, and offline repositories of different organizations and decide whether to remove data in own repository or whether to copy data across from external repository. ​
- UC5: A user can access a collaborative platform and discover, visualize, and process data hosted by different repositories (online, near-line, offline).
- UC6: Any federated organisation interested in collecting metrics about requests originated from external organization.​

Some example data from free and open datasets have been selected to be hosted in repositories on both ESA and DLR side. This example data is also made available and discoverable in ESA and DLR STAC catalogues (see picture below).


```{image} img/ESA_DLR_Demonstrator_STAC.png
:alt: ESA DLR Demonstrator Federated STAC catalogues
:width: 90%
:class: image-spaced
```


On ESA and DLR side an Identity and Access Management (IAM) system manages digital identities (accounts) of ESA and DLR users, respectively.
Both IAM act as Service Provider for the ESA / DLR service that hosts the restrained datasets (the ESA IAM protects the ESA repository, the ESA IAM protects the DLR repository).
As Identity Providers, both ESA and DLR IAM are configured to form a ESA/DLR Demonstrator Identity Federation.


```{image} img/ESA_DLR_Demonstrator_Building_Blocks.png
:alt: ESA DLR Demonstrator Building Blocks: Federated Identity Providers, federated services.png
:width: 90%
:class: image-spaced
```

This allows ESA users to use their ESA accounts to access data hosted in the DLR repository (and vice versa):
- an ESA user finds restrained data of interest hosted in the DLR repository using the federated discovery functionality
- when accessing the restrained data the user is asked to login
- instead of logging in with a local DLR account (stored in the DLR IAM) an option to login with ESA credentials is offered
- the ESA user clicks "Login with ESA account", is forwarded to the ESA IAM where the existing login session of the ESA user is detected
- the ESA IAM generates an authentication token and submits it to the DLR IAM
- the DLR IAM trusts the ESA IAM authentication token, generates a local authentication token and submits it to the DLR repository
- the DLR repository detects that the ESA user is authenticated, checks the authorization information contained in the token, and if authorized provides access to the restrained data.

## eduGAIN
### Overview
eduGAIN is a global meta-federation that interconnects national research and education identity federations worldwide {cite}`eduGAIN`. It enables students and researchers to access international digital services using their home institution credentials through single sign-on. By establishing a common trust framework and technical standards, the system ensures secure interoperability between participating organizations across different countries. This infrastructure eliminates the need for separate accounts, significantly simplifying collaboration for the global academic community. Operated by GÉANT, the platform empowers international research cooperation by standardizing identity management and facilitating seamless access to shared resources.

### Participation
Participation in eduGAIN is possible both as Service Provider (SP) or Identity Provider (IdP), but not directly. As a meta-federation, eduGAIN is a federation of national identity federations (e.g. _Canadian Access Federation_ (Canada), _Canadian Access Federation_ (France), _IDEM_ (Italy) or DFN-AAI (Germany); for a list of participating national federations see https://reporting.edugain.org/federation_list.php).

#### Participation as Service Provider
To participate as a Service Provider, your organization cannot join eduGAIN directly but must instead register through your national research and education federation. Begin by contacting your national federation's support team to initiate the onboarding process for your specific service. You must configure your service to meet technical requirements, typically involving SAML 2.0 compliance and specific attribute release policies. Your national federation will validate your service against their policies before including it in their local metadata. Once validated, your service metadata is aggregated into the global eduGAIN metadata feed, making it visible to users worldwide. This setup allows international researchers to access your service seamlessly using their home institution credentials.

#### Participation as Identity Provider
To participate as an Identity Provider, your organization must first join your national or regional research and education federation, as direct membership in eduGAIN is not available. Contact your national federation's support team to register your identity system and agree to their participation policies. You will need to ensure your technical infrastructure complies with SAML standards and eduGAIN's attribute release requirements. Once your national federation validates your configuration and legal agreements, they will publish your metadata to the eduGAIN meta-federation. This process enables users from other participating countries to authenticate using your institution's credentials. Ultimately, this expands your institution's reach by allowing global researchers to access your resources securely.

### AARC Blueprint Architecture
The AARC Blueprint Architecture {cite}`AARC_BPA` establishes a comprehensive reference model for identity and access management within the research and education sector. It defines the technical and policy standards necessary to achieve seamless interoperability between distinct identity federations. Serving as the foundation for eduGAIN, this blueprint ensures that participating national federations can trust and exchange identity data securely across borders. The architecture specifies critical protocols and attribute release policies that govern how users authenticate and access remote services. This standardization allows researchers to maintain a consistent digital identity regardless of their specific location or institution. Consequently, the AARC Blueprint acts as the essential technical backbone that sustains the global connectivity and trust model of eduGAIN.

The AARC Blueprint Architecture also serves as a rich source of Information, Guidelines and Best Practices on all levels of technical, organisational, legal (as far as possible) and security matters around identity federation topics {cite}`AARC_Guidelines`.

### References
<mark>Note</mark> _[UR]: references are now converted to bibtex entries. If citing works this section will be removed_


## EOEPCA+ - Earth Observation Exploitation Common Architecture

Cloud-based platforms have proven to be an essential cornerstone for a paradigm shift in Earth Observation (EO), suitable to allow science and application initiatives to efficiently manage the huge volume of data availability in a “bring-the-user-to-the-data” paradigm. This paradigm has been demonstrated to be a critical enabler of innovation and acceleration, which in the European context needs to leverage a fragmented cloud and platform ecosystem, developed with a multitude of industrial and public investments at European and National level.

EOEPCA+ is an ESA initiative whose objective is to define a Common Architecture for an exploitaiton platform that encourages interoperability and federation across the European EO cloud and platform ecosystem, by defining a set of common standards and interoperable Building Blocks (BBs) that can be shared across the different platforms and clouds. The aim is to support the EO Science, R&D, and applications community in their utilisation of the EO data and services, by allowing them to easily access and use the data and services across the different platforms and clouds, while also allowing them to share their data, code, and project results with the community on cloud-based environments.

```{image} img/eoepca-plus.webp
:alt: EOEPCA+
:width: 90%
:class: image-spaced
```

The EOEPCA+ architecture is supported by a Reference Implementation that helps to validate the architecture, and also provides a set of reusable capabilities for platform integrators - including resource catalogue and discovery, data access & visualisation, processing and workflow management, and identity and access management (IAM), and more. The architecture is designed to be modular and extensible, allowing for the integration of new capabilities and services as needed.

A key aspect of the EOEPCA+ architecture is the definition of a common authentication and authorization framework that allows users to access and use the data and services across the different platforms and clouds, while also allowing them to share their data, code, and project results with the community on cloud-based environments. This is expressed through the IAM Building Block that encapsulates the approach and provides a reusable reference implementation.

### EOEPCA+ Use Cases - Introduction

As a common reference architecture, that is not tied to any concrete platform, EOEPCA+ offers here generic use cases for Federated Authentication and Authorization, that can be used as a reference for other platforms that want to implement similar capabilities. These use cases are defined in the context of the EOEPCA+ architecture, but they are not limited to it, and they can be adapted and implemented in other contexts as well.

### EOEPCA+ Use Cases - Abstract Platform Federation

This use case describes a generic scenario of platform federation, where a user can access and use data and services across multiple platforms, without needing to log in separately to each platform. The key aspects of this use case are:

* User working across multiple platforms, with a dedicated user profile (account) in each platform, and no assumption of a shared IdP amongst the platforms - i.e. assume user maintains separate credentials for each platform.
    > alternative path where there is a shared IdP

* User authenticates to one platform (in the federation) and is granted access (within their permissions) to all federated platforms. This could be for accessing data, or for initiating processing etc.

* The user ID is unambiguously mapped from one platform to the other
    > maybe not needed if the IdP is shared

* User is able to establish workflows within one platform that chains steps across multiple platforms, without needing to log in separately to each platform, and without needing to manage separate credentials for each platform

* Trust relationships are established amongst the federated platforms

* Tokens are either accepted cross-platform, or are otherwise exchanged/transformed for consumption at the 'other' platform - with possible scope reduction

## SSI Decentralised
<img width="1440" height="317" alt="image" src="https://github.com/user-attachments/assets/258fc2a4-4732-4a58-bb26-8918c423b8c7" />

**S**elf-**S**overeign **I**dentity (SSI) is an approach to digital identity that gives individuals control over the information they use to prove who they are to websites, services, and applications across the web. 

[Self-sovereign identity Wikipedia](https://en.wikipedia.org/wiki/Self-sovereign_identity)

### COVID-19 vaccination in Japan

Digital Agency in Japan released an application for [“Certificate of COVID-19 Vaccination”](https://www.digital.go.jp/en/policies/vaccinecert) in 2021.  
It is an implementation by using VCs, and it took standards “SMART Health Card(SHC)”.  
SHC is developed by “Vaccination Credential Initiative(VCI), and it is discussed by Microsoft, Amazon Web Service, Oracle and so on.  

<img width="4402" height="1339" alt="COVID-19app" src="https://github.com/user-attachments/assets/a47fa2c7-6d08-4abe-8b94-66370b60e10c" />

### Community service wallet

**Toyonon Wallet** is an application for community service wallet inspired by the official mascot character of Toyono Town in Osaka, Japan, created to promote the town's community activities and local charm.

Toyonon wallet stores
- DID（Decentralized Identifier）
- Verifiable Credentials（VC）
- Digital coupon / voucher

<img width="1024" height="403" alt="image" src="https://github.com/user-attachments/assets/9cdb4cf8-fd81-48e0-a0d1-edc79d6503d6" />

Reference: [japanese](https://digitalplatformer.co.jp/220607002/)  
Reference: [platform](https://digitalplatformer.co.jp/en/20250312_01/)


### Japan’s Academic VC Pilots

Japan is actively advancing the practical adoption of Verifiable Credentials (VC) and Decentralized Identifiers (DID) within higher education to modernize academic credentialing and identity verification. Two prominent initiatives demonstrate this trend:

1. National Institute of Informatics (NII) – Academic VC Pilot  
  The National Institute of Informatics (NII) leads a pioneering Academic VC Pilot project aimed at issuing and managing digital academic credentials in a secure, privacy-preserving manner.  
  Overview: NII developed a digital student ID system leveraging VC and DID technology, enabling students to receive tamper-proof, cryptographically verifiable credentials representing their academic records and enrollment status.  
  Technology: Using globally recognized standards (W3C Verifiable Credentials), the system allows credential holders to control and selectively disclose their information without relying on centralized authorities.  
  Impact: This pilot validates the use of VC in authenticating academic qualifications and streamlines interactions with educational institutions and third parties (e.g., employers), enhancing trust and efficiency.  
  Reference: [Center for Trust and Digital Identity – Academic VC Pilot](https://trustdigitalidcenter.jp/?page_id=294&lang=en)  

2. Keio University – Verifiable Digital Student Credentials  
  Keio University has conducted successful trials issuing verifiable digital student credentials to enhance academic identity management.  
  Overview: Students receive digital certificates (such as enrollment verification and graduation diplomas) in the form of Verifiable Credentials issued via a secure, blockchain-backed platform.  
  Benefits: These credentials are cryptographically signed by the university, enabling instant verification by employers or external organizations without intermediary contact, reducing administrative overhead.  
  User Experience: Students can store and present their credentials on personal devices, maintaining privacy while facilitating seamless proof of academic status.  
  Reference: [Microsoft Customer Story – Keio University](https://www.microsoft.com/en/customers/story/1349421307379340138-keio-university-higher-education-azure-active-directory)

<!--
# Centralised vs Decentralised

This chapter examines the trade-offs between centralised and decentralised approaches to federated authentication and authorization.


## Definitions

TBD

- Self-Sovereign Identity

- “Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness”. SOURCE: [W3C PROV](https://www.w3.org/TR/prov-overview/).

- “Data integrity is the opposite of data corruption. The overall intent of any data integrity technique is the same: ensure data is recorded exactly as intended”. SOURCE: [Wikipedia](https://en.wikipedia.org/wiki/Data_integrity).

- “Trust is the characteristic that one entity is willing to rely upon a second entity to execute a set of actions and/or to make set of assertions about a set of subjects and/or scopes”.  SOURCE: [OASIS](https://docs.oasis-open.org/wss-m/wss/v1.1.1/os/wss-SOAPMessageSecurity-v1.1.1-os.html).
-->



## Integrity Provenance and Trust


The OGC Testbed-20 and OGC Testbed-21 activities included specific tasks related to Integrity, Provenance and Trust (IPT).
The Engineering Report OGC 24-033 {cite}`OGC_24-033` presents a number of IPT use cases that were explored and prototyped during the Testbed-20 activities. The objective was to propose new IPT building blocks that are aligned with existing OGC building blocks (API) and adhere to FAIR principles.  

### Decentralized identifiers

The W3C DID specification {cite}`W3C_DID` defines Decentralized identifiers (DIDs) as a new type of identifiers that enable verifiable, decentralized digital identity. A DID refers to any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) as determined by the controller of the DID. In contrast to typical, federated identifiers, DIDs have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. 

One of the [design goals](https://www.w3.org/TR/did-core/#design-goals) of DIDs is to be system- and network-independent and enable entities to use their digital identifiers with any system that supports DIDs and DID methods.

DIDs resolve to DID Documents that contain information about the public keys that are used by consumers of Verifiable Credentials (VC) {cite}`W3C_VC` and Verifiable Presentations (VP) to verify proofs (signatures).  

`DID Resolvers` are components that perform DID resolution by taking a DID as input and produce a conforming DID document as output.  This allows for the generation of abstractions of the underlying infrastructure which may be the [European Blockchain Service Infrastructure](https://ec.europa.eu/digital-building-blocks/sites/display/EBSI/Home) EBSI {cite}`EBSI_DID`, a distributed ledger such as [Indy](https://hyperledger.github.io/indy-did-method/), or an infrastructure serving Web DIDs {cite}`WEB_DID`.


In the `EO data supply chain` scenario of the Testbed-20 IPT activities, Decentralized Identifiers (DIDs) were used for identifying organizations and EO resources (products). 

The objective of this IPT scenario was to allow downstream EO data consumers, for example a third-party 'Watermarking' process, to “trust” the data, i.e., allow verification that data consumed is from the original data provider and allow verification of the integrity of the data.

### Verifiable credentials

In addition, EO resources were described with W3C Verifiable Credentials and Verifiable Presentations.   Verifiable Credentials are a novel way to express information as metadata, claims and proofs (signatures).  The Verifiable Credentials and Presentations are cryptographically verifiable using key information related to the DID identifying the holder and/or issuer.  In the described scenario, the `claims` correspond to EO product metadata properties, i.e. JSON(-LD) encoded EO product metadata.

To protect integrity of content of external link targets, e.g. product download links, quicklook links, multibase mulithash approaches were prototyped as proposed by W3C VC 1.1 (Hashlink) and VC 2.0 (Related Resource).

Verifiable Credentials (VC) and Presentations (VP) are exchanged between (VC) issuers, holders and verifiers.  An Indy-based `Verifier` process was demonstrated to be able to verify VC retrieved from an OGC API-Records/ STAC API compliant catalogue from a `Holder` organisation.  This organisation acted as custodian of data and metadata from data providers acting as `Issuer`.


```{mermaid}
sequenceDiagram

participant v as Verifier<br>(Data Consumer)
participant h as Holder<br>(Data Custodian)
participant issuer as Issuer<br>(Data Provider)

rect rgb(125,125,125,.2)
  note over v,Registry: Onboarding organisations
    issuer -->> Registry:Register DID
    h -->> Registry:Register DID
end
h -->>  issuer: VC Request
issuer -->> issuer: Sign VC
issuer -->>  h: Signed VC
h -->> Registry: Request DID<br>Document Issuer
h -->> h: Check VC signature

rect rgb(125,125,125,.2)
  note over v,Registry: Loop [Consuming (meta)data]
    v ->> h: VP Request
    h -->> h: Include signed VC in VP
    h -->> h: Sign VP
    h -->> v: Signed VP

    v -->> Registry: Request DID Document of Holder
    v -->> Registry: Request DID Document of Issuer
    v -->> v: Check VP signatures
end
```
Figure 1 - Verification of VC and VP (OGC 24-033)


The OGC Testbed-21 included a similar task called "Data Quality for Integrity, Provenance and Trust" (DQ4IPT).
The objectives of the task were as follows:

- Explore the integration of data quality considerations into IPT frameworks in such a way that users of Earth Observation data can have confidence in the data they use for analysis.
- Develop a reference architecture that integrates data quality considerations into IPT frameworks
- Demonstrate how the reference architecture can improve confidence in Earth Observation data
 
The activity aimed to provide a standards-based approach through which data producers such as space agencies can document and communicate the quality of their data products in a way that is both human and machine readable.

The Engineering Report OGC 26-005 {cite}`OGC_26-005` presents two IPT server implementations that were prototyped during the Testbed-21 activities:

The first implementation (D101) provided an OGC API-Process implementation with a, process that stored metadata of generated products in a STAC Catalog on a Hyperledger Fabric blockchain. The proces also stored the actual data it generates on an IPFS (Interplanetary File System) giving each resource a unique CID content identifier based on a cryptographic hash. The process acts as a Verifier of Verifiable Credentials (VC) provided with the input data.  The Verifiable Credantials related to "subjects" from multiple organisations (so-called "issuers") identified by their W3C DID which resolves to a DID document as in Testbed-20.

The second implementation (D102) hosts an API-Records/STAC-API Catalogue with STAC and ISO19115-4 metadata including quality and provenance information.  The IPT framework underneath is an evolution of the implementation in Testbed-20.  In the STAC Catalogue, each collection, granule and organisation is identified by a W3C DID identifier.   All granules havd a DID included in the metadata via the STAC Additional Identifiers extension.  The VC for a granule (similar to a verifiable "product passport") are accessible as STAC assets or links and embed OGC 17-003r2 metadata.  The VC apply content integrity protection of referenced information using the W3C VC model 2.0.

The simulated environment consists of various organisations (space agencies) that self-identify by having created a resolvable DID and associated DID document.  Verifiable Credentials (VC) for granules are issued by the corresponding organisations, which can be verified downstream by validating the VC using the public key information published by the corresponding organisations in their DID documents.

For examples of the various artifacts, we refer to both Engineering Reports:

- [W3C DID Document](https://docs.ogc.org/per/24-033.html#_w3c_decentralized_identifier_document_example)
- [W3C Verifiable Credential](https://docs.ogc.org/per/24-033.html#_w3c_verifiable_credentials_example)
- [W3C Verifiable Presentation](https://docs.ogc.org/per/24-033.html#_w3c_verifiable_presentations_example)

### Additional topics

Other Self-Sovereign Identity (SSI) aspects with W3C compliant VC/VP were identified as future work in the Engineering Report OGC 24-033 {cite}`OGC_24-033`:

- Integration with OpenID Connect (OIDC) and OAuth: “OpenID for VC/VP” (OID4VC, OID4VP) {cite}`OIDC_VC`.
- Decentralized Identifiers for individuals (“natural persons”), recorded in a “wallet.” In Testbed 20, EO use cases were limited to “legal persons” (DID recorded in a Registry instead of a wallet).
- Support for privacy and confidentiality via “Selective disclosure” (i.e., ability of a holder to decide what information to share, VC formatted according to a verifier’s data schema).

## Use Case Summary Table

| Use Case Example    | Key Technologies Applied | AuthN |AuthZ | Objectives |PoC|
| -------- | ------- | ------- |------- |------- |------- |
|    ESA/NASA MAAP     |     |  |    |   Cross-platform data retrieval, analysis, processor deployment and execution. Federated IdPs.  |   |
|    JAXA/ESA MAAP  |      |     |     |     |   |
|    NASA Use CASE (WGISS-59)  |      |     |     |     |   |
|    DestinE  |   |    |    |  Federated IdP, Federated services.  |   |
|    Bilateral ESA-DLR  |  identity federation | yes | yes |    | Demonstrator for federated discovery / federated access use cases |
|    eduGAIN  | applied AARC Blueprint Architecture | yes | yes | International Meta-Federation of national Identity Federations |   |
|    EOEPCA+  |  |  |  |   |   |
|    Japan SSI Decentralised  |   |    |    |    |   |
|    Integrity Provenance and Trust  |   |    |    |    |   |

