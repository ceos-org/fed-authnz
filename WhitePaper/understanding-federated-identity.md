# Understanding Federated Identity: Core Concepts and Protocols

This chapter covers the fundamental concepts and protocols that underpin federated identity systems.

## Essential Terminology
- **Authentication (AuthN):** The process of verifying a user's identity via a set of credentials such as username and password. It answers the question: _Who are you?_
- **Authorization (AuthZ):** The process of determining what actions or resources an authenticated user is allowed to access. It answers the question: _What are you allowed to do?_
- **Accounting and Quota Management:** Accounting is the process of keeping track of resource consumption (e.g. number of downloads, CPU time used). Accounting is a pre-requisite for Quota Management which allows limiting or throttling resource consumption. It answers the question: _How much did I already consume of a specific ressource?_. Accounting is also a pre-requisite of Billing (if required).
- **Federation:** A collection of organizations that agree to interoperate under a certain rule set. It answers the question: _Who vouched for you?_
- **Identity Federation:** A collection of organizations that agree to interoperate as Identity Providers (IdP). Main purpose is to allow access to a protected service no matter what IdP is used for authentication.
- **Data Federation:** A collection of organizations that agree to interoperate as Service Providers (SP). Main purpose is to allow access to several services. The services may require authentication via an IdP or not (e.g. open federated STAC catalogues). 
- **Identity and Access Management (IAM)** refers to the framework of policies, processes, and technologies used to manage digital identities and control access to resources within an organization.
IAM ensures that the right individuals and entities have the appropriate access to technology resources at the right times, for the right reasons. IAM is crucial for:
   - Enhancing security by preventing unauthorized access.
   - Supporting compliance with regulations like GDPR.
   - Improving user experience by enabling Single Sign-On (SSO) and streamlined access to resources.
- **IdP versus SP:** The Identity Provider (IdP) handles authentication and generates tokens providing the user's identity. The Service Provider (SP) handles authorization, validating the tokens from the IdP, and there enforces access control based on roles or permissions.
- **Policy Decision Point (PDP):** In the authorization context, the PDP is the decision engine that decides on the basis of applicable policies and relevant information (user attributes, etc.) if access can be granted or not.
- **Policy Enforcement (PEP):** In the authorization context, the PEP is the gatekeeper that enforces the decision of the PDP. Typically the PEP resides at the SP.
- **Policy Information Point (PIP):** In the authorization context, the PIP is the service where the PDP can request additional information required to decide an authorization request.
- **Single Sign-on (SSO):** SSO is an authentication scheme that allows a user to log in with a single ID to any of several related, yet independent, software systems within an organization. True single sign-on allows the user to log in once and access services without re-entering authentication factors.
- **Single Logout (SLO):**  SLO, as counterpart to SSO, is the mechanism by which a user is able to sign-out (logout) of all of the applications they signed into with single sign-on (SSO) including the identity provider.

## User Access Process
1. User Authentication: The user verifies their identity, typically via an Identity Provider (IdP), to initiate access. This step is crucial in federated systems where authentication is delegated across domains.
2. Role Activation: Once authenticated, the user's roles and permissions are determined, often conveyed through protocol-specific tokens or assertions (e.g., claims in OIDC or attributes in SAML).
3. Access Application / Services: Based on the authenticated identity and activated roles, the user is authorized to access protected applications or services, with access tokens (OAuth 2.0) or assertions (SAML) facilitating secure communication.
   
## Foundation Protocols Driving Federation

Federated identity protocols like OAuth 2.0, OpenID Connect (OIDC), and SAML are designed to support and secure each step of the user access process, enabling trusted identity verification, role-based access control, and seamless service authorization across organizational boundaries.

<img width="460" height="360" alt="image" src="https://github.com/user-attachments/assets/da5e7a57-3a8b-4fe8-9bdf-8e6189c77dc9" />


  - **OAuth 2.0**: Open Authorization 2.0 (OAuth 2.0) is an authorization standard that allows third-party applications to gain limited access to a user's resources without exposing their credentials.

<img width="488" height="288" alt="image" src="https://github.com/user-attachments/assets/fbc9ac54-4de4-44d7-ab55-6f7c06d9bbb5" />

  - **OIDC**: OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0 to provie authentication. It allows useres to log in using a third-party identity provider.

<img width="588" height="303" alt="image" src="https://github.com/user-attachments/assets/d042228a-c239-4af1-9602-40968d09e79a" />

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/8ff81ffc-ff8d-4356-a128-68b85b3a7c1a" />

  - **OAuth/OIDC**: This shows a summary of the various Oauth/OIDC flows and their associated features
  
  - **SAML**: Security Assertion Markup Language (SAML) is an open-standard XML-based data format that allows secure sharing of authentication and authorization data between different organizations or systems. It allows a user to log in once (via their organization's identity provider) and then access various partner applications or enterprise services without needing to re-enter credentials. SAML is used by both the IdPs and SPs within federated identity management setups. 


```{mermaid}
sequenceDiagram
    title OAuth 2.0 Authorization Code Flow (Simplified)

    actor User
    participant Client as Client Application
    participant AS as Authorization Server
    participant RS as Resource Server

    User->>Client: Initiates action requiring protected resource
    Client->>AS: Redirect to authorization endpoint
    AS->>User: Authenticate user and request consent

    User-->>AS: Authentication + consent approval
    AS-->>Client: Authorization code

    Client->>AS: Exchange authorization code for access token
    AS-->>Client: Access token

    Client->>RS: Request resource with access token
    RS-->>Client: Protected resource
```

### OpenID Connect (OIDC)
- **OIDC**: OpenID Connect is an identity layer built on top of OAuth 2.0 to provide authentication. It allows users to log in using a third-party identity provider.

```{mermaid}
sequenceDiagram
    title OpenID Connect Authorization Code Flow

    actor User
    participant Client as Client Application (RP)
    participant OP as OpenID Provider
    participant RS as Resource Server

    User->>Client: Initiates login or protected action
    Client->>OP: Redirect to authorization endpoint (OIDC request)
    OP->>User: Authenticate user and request consent

    User-->>OP: Authentication + consent approval
    OP-->>Client: Authorization code

    Client->>OP: Exchange code for tokens
    OP-->>Client: ID token + access token

    Client->>Client: Validate ID token (issuer, signature, claims)

    Client->>RS: Request resource with access token
    RS-->>Client: Protected resource
```

### Delegated OIDC
- **Delegated OIDC**: This flow shows how a local broker can use a home OpenID Provider (OP) to authenticate a user and map that identity back to a local service.

```{mermaid}
sequenceDiagram
    title Delegated Authentication with OpenID Connect (Federated)

    actor User
    participant RP as Receiving Platform (RP / MAAP)
    participant Broker as Local IAM / Broker
    participant OP as Home OpenID Provider

    User->>RP: Access protected platform
    RP->>Broker: Authentication required

    Broker->>OP: Redirect (OIDC auth request)
    OP->>User: Authenticate user

    User-->>OP: Credentials / MFA
    OP-->>Broker: Authorization code

    Broker->>OP: Token request
    OP-->>Broker: ID Token + Access Token

    Broker->>Broker: Validate ID Token
    Broker->>Broker: Map subject → local identity

    Broker-->>RP: Authentication result
    RP-->>User: Access granted
```

### Delegated Authentication
- **Delegated Authentication via Federated Identity Provider**: When a user from one organization accesses a service in another, the local environment delegates authentication to the user's home Identity Provider.

```{mermaid}
sequenceDiagram
    title Delegated Authentication via Federated Identity Provider

    actor User
    participant SP as Service / Platform
    participant HomeIdP as Home Identity Provider
    participant IAM as Local IAM (Broker)

    User->>SP: Access protected platform
    SP->>IAM: Authentication required

    IAM->>HomeIdP: Redirect for delegated authentication
    HomeIdP->>User: Authenticate user

    User-->>HomeIdP: Credentials / MFA
    HomeIdP-->>IAM: Authentication assertion

    IAM->>IAM: Validate assertion
    IAM->>IAM: Map to local identity
    IAM-->>SP: Authentication result

    SP-->>User: Access granted
```

  - **SAML**: Security Assertion Markup Language (SAML) is an open-standard XML-based data format that allows secure sharing of authentication and authorization data between different organizations or systems. It allows a user to log in once (via their organization's identity provider) and then access various partner applications or enterprise services without needing to re-enter credentials. SAML is used by both the IdPs and SPs within federated identity management setups.

## Types of Federation (or: Federation Taxonomy?)
<mark>Note</mark> _[UR]_ initial content/structure for this new section. Just a proposal, please add/update/comment.

### Overview
_Federating something_ means making a resource or asset inside an organization accessible to one or more other organizations.
An organization may federate different types or resources or assets: Identities, Services, Data, Catalogues etc. (see section _Federation Types: Type of federated Ressources_ below).

Federations vary extremely in size: from 1:1 bilateral federations with two participants up to n:m (IdP:SP) open federations with a varying and sometimes very high number of participants (example: eduGAIN).

The type of information exchanged between participants in a federation also has legal and compliance implications. If personal data of users is transferred between participants of a federation data protection requirements must be met. Depending on the type of data exchanged, additional legal requirements may apply, too (e.g. export control law).



### Federation Types: Type of federated Ressources

Identities, Data, Catalogues, ...

### Federation Types: Federation Size / Number and organizational structure of Participants

Identity Federation = cross-organizational version of SSO

from 1:1 to n:m 

### Federation Types: Geolocation of Participants, national / international Federations

inside a single jurisdiction vs. cross-jurisdictional

### Federation Types: closed versus open Federations

bilateral, trilateral, ... - fixed number of participants. allows to establish a federation contract between participants to define federation details, responsibilities, ...

open Federations: e.g. national research Identity Federations, eduGAIN: participating IdPs and SPs changes over time
contract between all participants is not feasible
-> Solution: 












---
Used and useful references: 

[Foundation Protocols Driving Federation](https://auth0.com/docs/authenticate/protocols)

[Data Space Support Centre - Data Sovereignty and Trust Pillar](https://dssc.eu/space/bv15e/766068339/Data+Sovereignty+and+Trust)

[European Identity Wallet Reference architecture](https://digital-strategy.ec.europa.eu/en/library/european-digital-identity-wallet-architecture-and-reference-framework)

