# Generated Mermaid Diagrams

This file is generated from Mermaid source files in `WhitePaper/img`.

### Delegated Authentication via Federated Identity Provider

```mermaid

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

    IAM->>IAM: Validate assertion\nMap to local identity
    IAM-->>SP: Authentication result

    SP-->>User: Access granted
```

### delegated oidc

```mermaid
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

    Broker->>Broker: Validate ID Token\n(issuer, audience, signature)
    Broker->>Broker: Map subject → local identity

    Broker-->>RP: Authentication result
    RP-->>User: Access granted
```

### OAuth 2.0 Authorization Code Flow

```mermaid

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

### OpenID Connect Authorization Code Flow

```mermaid

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

