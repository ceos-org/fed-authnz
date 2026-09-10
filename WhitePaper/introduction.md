# 1. Federated EO Access: Executive Overview & Introduction

This chapter introduces the evolving landscape of digital and unified Earth Observation (EO) access, setting the foundation for understanding federated authentication and authorization in the context of EO data systems.
The Committee on Earth Observation Satellites (CEOS) coordinates international civil space-based Earth observation (EO) programmes and promotes the exchange and use of EO data for societal benefit and informed decision-making. Within CEOS, the Working Group on Information Systems and Services (WGISS) supports this mission by advancing the systems, services, standards and collaborative practices needed to discover, access, manage and use EO data across organisational and national boundaries.

The EO information landscape has changed significantly. The growing number of missions, data providers, cloud platforms and analysis services gives users access to an unprecedented range of observations and capabilities. At the same time, many applications—including climate monitoring, disaster response, environmental assessment and scientific research—depend on combining data and services from several missions and organisations rather than working within a single provider environment. Increasingly, these activities also rely on automated, machine-to-machine and cloud-based workflows.

WGISS activities, including Connected Data Assets and common discovery best practices, help users locate resources distributed across agencies. The CEOS Interoperability Handbook {cite}`Interop_Handbook` complements this work promoting a common framework for improving the interoperability of EO data and services, including recommendations for authentication and authorization based on open standards. Together, these activities provide the context for addressing a further challenge: enabling users and applications to move consistently and securely from discovering resources to using them.

However, the ability to discover a resource does not necessarily provide a seamless path to using it. Users may still need to create and manage separate accounts, repeat authentication steps, and navigate different access rules across agency data archives, cloud platforms, processing services and collaborative environments. These barriers become more significant when workflows cross organisational boundaries or must operate without continuous user interaction. 

## 1.1 The Modern Dilemma: Why Unified EO Access is Critical

Discoverability alone does not guarantee straightforward access. Users working across archives and analysis platforms may encounter separate registrations, repeated logins and different access procedures. Developers must accommodate these differences when connecting services, adding integration effort and potential interruptions to scientific workflows.

Cloud-based processing and automated access make this challenge more significant. A workflow may need to retrieve protected data or invoke services across several platforms without repeated manual intervention. Here, unified access means a more consistent experience across participating systems, while respecting the access conditions of each resource.

## 1.2 The Federated Solution: Authentication & Authorization

Authentication establishes who a user or system is, while authorization determines which resources and actions that identity is permitted to access. In most EO environments, both functions are implemented locally. This allows each provider to retain control of its resources, but it can also create a fragmented experience for users and make cross-platform integration more complex.

Federated authentication and authorization offer a way for participating organisations to establish trust and exchange identity or access information using agreed policies and open technical standards. A user may authenticate through an existing or “home” identity provider and use that trusted identity to request access to services operated by other organisations. For machine-to-machine workflows, federation may also support secure delegation or token exchange between services, reducing the need to distribute and maintain separate long-lived credentials.

Based on agreed trust arrangements and open standards, federation can reduce repeated credential management and support cross-platform workflows. Its implementation also requires clear responsibilities for security, attribute exchange and privacy. The Handbook recommends open-standard authentication and support for both human and machine-to-machine access. Federation should complement, rather than add barriers to, resources available without authentication; discovery interfaces should remain accessible without login, consistent with that guidance.

For the CEOS community, federation has the potential to:

- reduce the number of credentials and repeated login processes that users must manage;
- enable more coherent access to distributed data, tools and processing environments;
- support cross-platform scientific workflows and collaboration among agencies;
- improve support for secure machine-to-machine access and scalable cloud processing;
- encourage the use of established standards rather than provider-specific access mechanisms; and
- strengthen security by allowing authentication capabilities, including multi-factor authentication, to be provided and managed by trusted identity providers.

Federation does not imply that CEOS should operate a single central identity system, nor that participating agencies must adopt identical access policies. Data and service providers remain responsible for deciding what an authenticated identity is permitted to do, in accordance with their own mandates, policies, licences, security requirements and applicable legal frameworks. 
A federated approach must therefore address not only protocols and system architecture, but also trust, governance, attribute exchange, privacy, accountability and cross-jurisdictional compliance.

## 1.3 Purpose & Audience

This White Paper provides a common reference for examining federated authentication and authorization in the CEOS EO ecosystem. It is intended to connect current agency experience and practical use cases with the broader interoperability objectives of CEOS and WGISS.

The document:

- introduces the core concepts, terminology and protocols used in identity federation;
- considers different federation models, including centralised, brokered and decentralised approaches;
- documents representative use cases and ongoing initiatives contributed by CEOS agencies and partners;
- identifies technical, organisational, policy, legal and compliance challenges; and
- outlines possible strategic directions, reusable patterns and areas for further cooperation or demonstration.

The White Paper is not intended to prescribe a single architecture or replace the access-control responsibilities of individual providers. Its purpose is to develop a shared understanding, identify common requirements and help the CEOS community assess where interoperability can be improved through standards, coordinated practices and incremental federation activities.

The intended audience includes CEOS agencies and partners, EO data and service providers, platform operators, developers and system architects, together with those responsible for identity management, security, policy and programme coordination, supporting informed decisions and identifying opportunities for further cooperation.
By bringing these perspectives together, the White Paper aims to support a practical path from isolated authentication systems towards trusted, interoperable access to distributed EO data and services—while preserving the autonomy and policy responsibilities of each participating organisation.


## 1.4 Where are we now? what should the future hold? 
Earth Observation (EO) missions produce vast amounts of data, supporting a wide range of stakeholders—including scientists, developers, and decision-makers worldwide. These stakeholders come from diverse institutions such as research centers, government agencies, and commercial organizations, each requiring access to different datasets and services.

EO data usage is often not centered around a specific mission, but rather around an application that benefits from sourcing any type of EO data that supports its purpose. The most user-centric approach would allow users to access as much data as possible from their home institution. In reality, however, the diversity of EO missions results in different data collections spread across platforms and agencies, leading to complex authorization scenarios and fragmented access control. Currently, authorization is handled locally by the data's host, often based on varying attributes. These differences can stem from political decisions—for example, European Commission (Copernicus Programme) versus ESA policies (EO Science missions), or GDPR versus U.S. data governance frameworks.

All of this contributes to a highly inconsistent user experience. Different datasets and services require different login flows, creating a landscape where scientists and stakeholders often spend as much time navigating and managing access as they do actually using the data. This time could be better invested in analysis and application if the data landscape were more streamlined.
Federation offers a way forward: it facilitates collaboration and shifts the focus toward actual EO data usage by simplifying inter-organizational access. However, it also introduces challenges, particularly around legal and compliance issues.

The use cases collected in this White Paper provide a basis for examining practical requirements and lessons from different approaches. They should not be read as evidence that a common CEOS-wide federation is already in place. Looking ahead, shared requirements, targeted demonstrations and comparison of benefits, costs and constraints could help agencies assess feasible next steps. The objective is to make collaboration and EO data use easier while retaining each provider's responsibility for its resources and access policies.


---

## Terms and Definitions

```{glossary}
DCS
    Data Centric Security

DID
    Decentralized identifier

EO
    Earth Observation

IPT
    Integrity Provenance Trust

ISO
    International Organization for Standardization

OGC 
    Open Geospatial Consortium

SSI
    Self-sovereign identity

VC 
    Verifiable Credential

VP 
    Verifiable Presentation

W3C
    World Wide Web Consortium 
```

## Reference Documents

```{bibliography}
:style: unsrt
```
