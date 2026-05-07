# Use Cases Definition

This chapter defines the specific use cases for federated authentication and authorization in Earth Observation systems.


## ESA/NASA MAAP

### Motivation and Scope

The ESA–NASA Multi‑Mission Algorithm and Analysis Platform (MAAP) is a jointly developed initiative comprising two independently operated but interoperable cloud‑based platforms. While operated under separate organizational governance, the ESA and NASA MAAPs share a common architectural vision, interoperability standards, and mission objectives, supporting missions such as BIOMASS, NISAR, and GEDI.

### User‑Centric Goals of MAAP Federation

_[SMB] The MAAP federation architecture is evolving; the level of technical detail presented here focuses on conceptual goals and intended capabilities rather than a finalized operational architecture._

The goal of federation between the ESA and NASA MAAP platforms is to enable seamless scientific collaboration across organizational boundaries while preserving platform autonomy. From a user perspective, federation enables scientists to access data, algorithms, and processing environments hosted on either MAAP using their existing organizational identity. From a platform perspective, federation supports controlled access to protected resources, interoperability of services, and coordinated execution of distributed workflows without requiring centralised identity or security infrastructure.

### Value‑Adding Cross‑Platform Use Cases

Federation between ESA and NASA MAAP platforms enables a set of use cases that directly support scientific workflows. These use cases focus on accessing, combining, and processing data across platforms, rather than on the mechanics of identity federation itself.

#### Federated Data Discovery and Access

Federated access enables users to discover and retrieve datasets hosted on either MAAP platform. Users search across distributed catalogues, access protected datasets, and retrieve data regardless of which organization hosts the underlying repository.

This capability supports common EO workflows where relevant data is spread across agency‑specific platforms and removes the need for users to maintain multiple accounts or navigate divergent access procedures.

#### Cross‑Platform Processing and Analysis

The joint MAAP architecture enables users to deploy and execute processing workflows across both platforms. From a user’s notebook or analysis environment, the same processor is executed against datasets hosted on different MAAPs by changing only the target endpoint.

This approach supports execution of the same processor across different datasets and enables users to retrieve and compare the outputs from both platforms to validate consistency.

### Federation as the Enabling Mechanism

The cross‑platform use cases described above rely on an established identity federation between ESA and NASA. Identity federation provides mutual recognition of user identities asserted by each organization’s Identity Provider and forms a foundational capability for controlled access to protected MAAP resources.

Identity federation is not an end in itself, but an enabling mechanism through which federated data access and processing use cases are realized in practice. Once established, it supports both interactive user access and non‑interactive platform‑level interactions.

### Federation Use Case: Bilateral Delegated Authentication and Entitlement Propagation

This use case illustrates how identity federation between ESA and NASA is realized in practice on the MAAP platforms, enabling secure, user‑centric access to protected EO resources across organizational boundaries while preserving local governance and authorization enforcement.

#### Context

The BIOMASS mission benefits from close collaboration between ESA and NASA partner infrastructures, enabling scientists to access Mission Analysis and Application Platform (MAAP) resources operated by both organizations. Users authenticate using their respective “home” Identity Providers (IdPs), while resources are hosted across organizational boundaries.

Entitlements are issued by the user’s home organization and made available to the hosting MAAP via federated interfaces; the authoritative source is platform‑specific and outside the scope of this use case.

Authorization decisions are enforced at the MAAP level and depend on entitlement information exchanged between peered MAAP platforms rather than solely on identity provider assertions.

#### Actors

- End User  
- Home Identity Provider  
- Partner Identity Provider  
- Peer platforms operated by ESA and NASA  
  - Home BIOMASS MAAP  
  - Hosting BIOMASS MAAP  

#### Preconditions

- The user holds an account at their home organization (ESA EOIAM or NASA EDL).
- The user has been granted the BIOMASS initiative entitlement at their home organization.
- A bilateral trust relationship exists between ESA EOIAM and NASA EDL.
- Federated entitlement exchange between peered MAAPs has been established.

#### Main Flow

1. The user initiates access to a protected BIOMASS MAAP hosted by the partner organization (e.g. an ESA user accessing a NASA MAAP).
2. The user authenticates using their home IdP (EOIAM or EDL).
3. On first use of the federation:
   - The user explicitly consents to the sharing of identity attributes on the originating side.
   - The user accepts applicable terms and conditions on the receiving side.
4. Upon successful authentication, the home IdP asserts the user’s identity and conveys a user identifier to the partner IdP.
5. The receiving IdP validates the assertion and maps the remote user to a local security context.
6. When accessing the MAAP environment, the hosting MAAP queries the peer MAAP for the user entitlement.
7. The user is granted access to BIOMASS MAAP resources according to the conveyed entitlement, independent of whether the service is hosted at ESA or NASA.

#### Postconditions

The user is treated as a first‑class user on the receiving infrastructure:

- Access control decisions are enforced locally.
- The user creates API tokens or credentials.
- The user performs actions supported by the MAAP according to their entitlement.

No separate user registration or account provisioning is required at the partner organization.

#### Key Properties

- Bilateral federation with mutual recognition of identities.
- Cross‑organization entitlement propagation.
- Explicit user consent and legal acceptance at first use.
- Operational equivalence between local and federated users.

```mermaid
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
Beyond interactive user access, the ESA and NASA MAAP platforms establish trust relationships that enable direct platform‑to‑platform interactions. These mechanisms support backend authorization, entitlement validation, and the orchestration of distributed workflows across platforms.
_[FWI] This area may evolve as platform capabilities mature; detailed protocol choices and implementation specifics are intentionally left out_

<img width="1000" height="650" alt="image" src="https://github.com/user-attachments/assets/4bc950b8-a91b-4d32-937c-907d230fa6c0" />

<img width="1000" height="350" alt="image" src="https://github.com/user-attachments/assets/a7dd75ee-e8ba-4312-9cb7-398869fa9409" />

[NASA MAAP](https://maap-project.org/)

[ESA MAAP (BIOMASS)](https://portal.maap.eo.esa.int/biomass/)

## NASA Use Case (WGISS-59) 

## DestinE 
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

<mark>Note</mark> _[UR]_ to be inserted: simplified graphic depicting the DLR and ESA STAC catalogues (similar to slide 7 of the Bilateral PPT)

On ESA and DLR side an Identity and Access Management (IAM) system manages digital identities (accounts) of ESA and DLR users, respectively.
Both IAM act as Service Provider for the ESA / DLR service that hosts the restrained datasets (the ESA IAM protects the ESA repository, the ESA IAM protects the DLR repository).
As Identity Providers, both ESA and DLR IAM are configured to form a ESA/DLR Demonstrator Identity Federation.

<mark>Note</mark> _[UR]_ to be inserted: simplified graphic depicting the DLR and ESA demonstrator components (similar to slide 18 of the Bilateral PPT)

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
eduGAIN is a global meta-federation that interconnects national research and education identity federations worldwide. It enables students and researchers to access international digital services using their home institution credentials through single sign-on. By establishing a common trust framework and technical standards, the system ensures secure interoperability between participating organizations across different countries. This infrastructure eliminates the need for separate accounts, significantly simplifying collaboration for the global academic community. Operated by GÉANT, the platform empowers international research cooperation by standardizing identity management and facilitating seamless access to shared resources.

### Participation
Participation in eduGAIN is possible both as Service Provider (SP) or Identity Provider (IdP), but not directly. As a meta-federation, eduGAIN is a federation of national identity federations (e.g. _Canadian Access Federation_ (Canada), _Canadian Access Federation_ (France), _IDEM_ (Italy) or DFN-AAI (Germany); for a list of participating national federations see https://reporting.edugain.org/federation_list.php).

#### Participation as Service Provider
To participate as a Service Provider, your organization cannot join eduGAIN directly but must instead register through your national research and education federation. Begin by contacting your national federation's support team to initiate the onboarding process for your specific service. You must configure your service to meet technical requirements, typically involving SAML 2.0 compliance and specific attribute release policies. Your national federation will validate your service against their policies before including it in their local metadata. Once validated, your service metadata is aggregated into the global eduGAIN metadata feed, making it visible to users worldwide. This setup allows international researchers to access your service seamlessly using their home institution credentials.

#### Participation as Identity Provider
To participate as an Identity Provider, your organization must first join your national or regional research and education federation, as direct membership in eduGAIN is not available. Contact your national federation's support team to register your identity system and agree to their participation policies. You will need to ensure your technical infrastructure complies with SAML standards and eduGAIN's attribute release requirements. Once your national federation validates your configuration and legal agreements, they will publish your metadata to the eduGAIN meta-federation. This process enables users from other participating countries to authenticate using your institution's credentials. Ultimately, this expands your institution's reach by allowing global researchers to access your resources securely.

### AARC Blueprint Architecture
The AARC Blueprint Architecture establishes a comprehensive reference model for identity and access management within the research and education sector. It defines the technical and policy standards necessary to achieve seamless interoperability between distinct identity federations. Serving as the foundation for eduGAIN, this blueprint ensures that participating national federations can trust and exchange identity data securely across borders. The architecture specifies critical protocols and attribute release policies that govern how users authenticate and access remote services. This standardization allows researchers to maintain a consistent digital identity regardless of their specific location or institution. Consequently, the AARC Blueprint acts as the essential technical backbone that sustains the global connectivity and trust model of eduGAIN.

The AARC Blueprint Architecture also serves as a rich source of Information, Guidelines and Best Practices on all levels of technical, organisational, legal (as far as possible) and security matters around identity federation topics.

### References
<mark>Note</mark> _[UR]: will be converted to bibtex references_
[Reference 1](https://)
[eduGAIN Hompage](https://edugain.org/)
[AARC Blueprint Architecture](https://aarc-community.org/))
[AARC Guidelines](https://aarc-project.eu/guidelines/)


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

## Use Case Summary Table

| Use Case Example    | Key Technologies Applied | AuthN |AuthZ | Objectives |PoC|
| -------- | ------- | ------- |------- |------- |------- |
|     ESA/NASA MAAP     |     |  |    |   Cross-platform data retrieval, analysis, processor deployment and execution. Federated IdPs.  |   |
|NASA Use CASE (WGISS-59)  |      |     |     |     |   |
|   DestinE  |   |    |    |  Federated IdP, Federated services.  |   |
|   Bilateral ESA-DLR  |  identity federation | yes | yes |    | Demonstrator for federated discovery / federated access use cases |
|   eduGAIN  | applied AARC Blueprint Architecture | yes | yes | International Meta-Federation of national Identity Federations |   |
|   SSI Decentralised  |   |    |    |    |   |

