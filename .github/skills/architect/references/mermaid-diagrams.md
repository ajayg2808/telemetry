# Mermaid Diagrams Guide

Mermaid is a JavaScript-based diagramming and charting tool that uses a simple, markdown-inspired syntax to create and modify diagrams dynamically. This guide provides comprehensive examples of using Mermaid to document architecture, design patterns, and data flow.

## Introduction to Mermaid

Mermaid renders markdown-like text definitions to dynamically create diagrams. It's perfect for architecture documentation because:

- **Version Control Friendly** – Diagrams are stored as text, making them easy to track in Git
- **Documentation-Integrated** – Renders directly in Markdown files and documentation
- **Quick Iteration** – Easy to update and modify without external tools
- **Consistent Styling** – Automatic diagram formatting and layout

## Class Diagrams

Class diagrams show the static structure of a system, including classes, interfaces, and their relationships.

### Basic Class Diagram Syntax

```mermaid
classDiagram
    class ClassName {
        +propertyName: type
        -privateProperty: type
        #protectedProperty: type
        ~internalProperty: type
        +methodName(param: type) returnType
        -privateMethod() void
    }
```

### Relationships in Class Diagrams

**Inheritance (Solid line with hollow arrow)**
```mermaid
classDiagram
    Animal <|-- Dog
    Animal <|-- Cat
```

**Interface Implementation (Dashed line with hollow arrow)**
```mermaid
classDiagram
    class Database {
        <<interface>>
    }
    Database <|.. PostgreSQL
    Database <|.. MongoDB
```

**Association (Solid line with arrow)**
```mermaid
classDiagram
    Employee --> Department
```

**Aggregation (Solid line with hollow diamond)**
```mermaid
classDiagram
    Department o-- Employee
```

**Composition (Solid line with filled diamond)**
```mermaid
classDiagram
    Human *-- Brain
    Human *-- Heart
```

### Complete Class Diagram Example

```mermaid
classDiagram
    class Repository {
        <<interface>>
        +create(entity: Entity)
        +read(id: ID) Entity
        +update(entity: Entity)
        +delete(id: ID)
    }
    
    class User {
        -id: UUID
        -email: string
        -password: string
        -createdAt: DateTime
        +getFullName() string
        +isActive() boolean
    }
    
    class UserRepository {
        -db: Database
        +create(user: User) void
        +findById(id: UUID) User
        +findByEmail(email: string) User
        +update(user: User) void
        +delete(id: UUID) void
    }
    
    class UserService {
        -repository: UserRepository
        +register(email: string, password: string) User
        +authenticate(email: string, password: string) AuthToken
        +updateProfile(id: UUID, changes: object) User
    }
    
    Repository <|.. UserRepository
    UserRepository --> User
    UserService --> UserRepository
    UserService --> User
```

### Class Diagram Multiplicity

Multiplicity indicates how many instances can participate in a relationship:

```mermaid
classDiagram
    Department "1" -- "0..n" Employee
    Project "1" -- "1..n" Task
    Company "1" o-- "*" Department
    Author "1" -- "1..*" Book
```

**Multiplicity notation:**
- `1` - exactly one
- `0..1` - zero or one
- `*` or `0..*` - zero or more
- `1..*` - one or more
- `n` - exactly n

## Flowcharts

Flowcharts describe processes, algorithms, and decision trees using a sequence of steps and decision points.

### Basic Flowchart Syntax

```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do Something]
    B -->|No| D[Do Something Else]
    C --> E[End]
    D --> E
```

### Node Types

```mermaid
flowchart TD
    A[Rectangle]
    B[/Parallelogram right/]
    C[\Parallelogram left\]
    D{Diamond}
    E([Rounded Rectangle])
    F[[Subroutine]]
    G[(Database)]
```

### Direction Options

- `TD` - Top Down
- `BT` - Bottom Top
- `LR` - Left Right
- `RL` - Right Left

### Flowchart Example: Data Processing Pipeline

```mermaid
flowchart TD
    Start([Start]) --> Ingest["Ingest Data<br/>from Source"]
    Ingest --> Validate{Valid<br/>Format?}
    
    Validate -->|No| LogError["Log Error<br/>Skip Record"]
    LogError --> Next{More<br/>Records?}
    
    Validate -->|Yes| Transform["Transform Data<br/>Apply Mappings"]
    Transform --> Enrich["Enrich Data<br/>Add Context"]
    
    Enrich --> Quality{Quality<br/>Check?}
    Quality -->|Failed| Quarantine["Quarantine<br/>for Review"]
    Quarantine --> Next
    
    Quality -->|Passed| Store["Store in<br/>Destination"]
    Store --> Next
    
    Next -->|Yes| Ingest
    Next -->|No| Complete([Completed])
```

### Flowchart Example: System Decision Flow

```mermaid
flowchart TD
    Request["Receive HTTP<br/>Request"] --> Auth{Authenticated?}
    
    Auth -->|No| Unauthorized["Return 401<br/>Unauthorized"]
    Unauthorized --> Log1["Log Auth<br/>Failure"]
    Log1 --> End1([End])
    
    Auth -->|Yes| Authorize{Authorized<br/>for Resource?}
    
    Authorize -->|No| Forbidden["Return 403<br/>Forbidden"]
    Forbidden --> Log2["Log Access<br/>Denied"]
    Log2 --> End2([End])
    
    Authorize -->|Yes| Validate{Valid<br/>Request?}
    
    Validate -->|No| BadRequest["Return 400<br/>Bad Request"]
    BadRequest --> End3([End])
    
    Validate -->|Yes| Process["Process<br/>Request"]
    Process --> Response["Return 200<br/>Response"]
    Response --> End4([End])
```

## Sequence Diagrams

Sequence diagrams show how components interact with each other over time, displaying the order and timing of message exchanges.

### Basic Sequence Diagram Syntax

```mermaid
sequenceDiagram
    participant A as Actor
    participant B as Service
    A->>B: Request
    B-->>A: Response
```

### Interaction Types

```mermaid
sequenceDiagram
    participant A
    participant B
    A->>B: Synchronous call (solid arrow)
    B-->>A: Response (dashed arrow)
    A-xB: Asynchronous (solid with x)
    A--xB: Async response (dashed with x)
```

### Activation Boxes

Activation boxes show when a component is active (processing):

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant DB
    
    Client->>API: POST /users
    activate API
    API->>DB: INSERT user
    activate DB
    DB-->>API: User created
    deactivate DB
    API-->>Client: 201 Created
    deactivate API
```

### Sequence Diagram Example: User Registration

```mermaid
sequenceDiagram
    participant User
    participant WebApp as Web App
    participant API as API Server
    participant DB as Database
    participant Email as Email Service
    
    User->>WebApp: Enter email and password
    activate WebApp
    
    WebApp->>API: POST /register
    activate API
    
    API->>DB: Check if email exists
    activate DB
    DB-->>API: Email available
    deactivate DB
    
    API->>DB: Create user record
    activate DB
    DB-->>API: User ID returned
    deactivate DB
    
    API->>Email: Send verification email
    activate Email
    Email-->>API: Email queued
    deactivate Email
    
    API-->>WebApp: 201 User created
    deactivate API
    
    WebApp-->>User: Registration successful
    deactivate WebApp
    
    User->>Email: Click verification link
    activate Email
    Email->>API: POST /verify
    activate API
    API->>DB: Mark email verified
    API-->>Email: Verified
    deactivate API
    Email-->>User: Account activated
    deactivate Email
```

### Sequence Diagram Example: API Request with Caching

```mermaid
sequenceDiagram
    participant Client
    participant Cache as Cache Layer
    participant API as API Service
    participant DB as Database
    
    Client->>Cache: GET /products/123
    activate Cache
    
    alt Cache Hit
        Cache-->>Client: Cached data
    else Cache Miss
        Cache->>API: GET /products/123
        activate API
        
        API->>DB: SELECT product
        activate DB
        DB-->>API: Product data
        deactivate DB
        
        API-->>Cache: Product data
        deactivate API
        
        Cache->>Cache: Store in cache (TTL: 1h)
        Cache-->>Client: Product data
    end
    deactivate Cache
```

## Entity Relationship Diagrams (ERD)

Entity-relationship diagrams show how entities (tables) relate to each other in a data model.

### Basic ERD Syntax

```mermaid
erDiagram
    ENTITY1 ||--o{ ENTITY2 : relationship
```

### Relationship Types

```mermaid
erDiagram
    A ||--o{ B : "one to many"
    C o|--|| D : "many to one"
    E ||--|| F : "one to one"
    G }o--o{ H : "many to many"
```

**Relationship notation:**
- `||` - exactly one
- `o{` - zero or more
- `}{` - one or more
- `o|` - zero or one

### Complete ERD Example

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    USER ||--o{ REVIEW : writes
    ORDER ||--|{ PRODUCT : contains
    PRODUCT ||--o{ CATEGORY : belongs
    PRODUCT ||--o{ REVIEW : receives
    ORDER ||--o{ PAYMENT : processes
    USER ||--o{ ADDRESS : has
    
    USER {
        int user_id PK
        string email UK
        string password_hash
        string first_name
        string last_name
        datetime created_at
        datetime updated_at
    }
    
    PRODUCT {
        int product_id PK
        string name UK
        text description
        decimal price
        int stock_quantity
        int category_id FK
    }
    
    CATEGORY {
        int category_id PK
        string name UK
        text description
    }
    
    ORDER {
        int order_id PK
        int user_id FK
        decimal total_amount
        string status
        datetime created_at
    }
    
    PAYMENT {
        int payment_id PK
        int order_id FK UK
        string method
        decimal amount
        string status
        datetime processed_at
    }
    
    REVIEW {
        int review_id PK
        int product_id FK
        int user_id FK
        int rating
        text comment
        datetime created_at
    }
    
    ADDRESS {
        int address_id PK
        int user_id FK
        string street
        string city
        string state
        string postal_code
        string country
    }
```

## State Diagrams

State diagrams model the states and transitions of a system or component.

### Basic State Diagram Syntax

```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2: Condition
    State2 --> [*]
```

### State Diagram Example: Order Processing

```mermaid
stateDiagram-v2
    [*] --> Pending
    
    Pending --> Confirmed: Confirm Order
    Pending --> Cancelled: Cancel
    
    Confirmed --> Processing: Start Processing
    Confirmed --> Cancelled: Cancel
    
    Processing --> Packaged: Package Items
    Processing --> Cancelled: Cancel
    
    Packaged --> Shipped: Ship Order
    Packaged --> Cancelled: Cancel
    
    Shipped --> InTransit: In Transit
    
    InTransit --> Delivered: Delivery Confirmed
    InTransit --> Failed: Delivery Failed
    
    Failed --> Reshipped: Reship
    Reshipped --> InTransit
    
    Delivered --> [*]
    Cancelled --> [*]
```

### State Diagram Example: User Session

```mermaid
stateDiagram-v2
    [*] --> Unauthenticated
    
    Unauthenticated --> Authenticating: Login Attempt
    Authenticating --> Unauthenticated: Auth Failed
    Authenticating --> Authenticated: Auth Success
    
    Authenticated --> Active: User Activity
    Active --> Idle: No Activity (timeout > 5min)
    Idle --> Active: User Activity
    Idle --> SessionExpired: Timeout > 30min
    
    Active --> LoggingOut: Logout
    Authenticated --> LoggingOut: Logout
    
    LoggingOut --> Unauthenticated
    SessionExpired --> Unauthenticated
```

## Architecture Diagram Best Practices

### Do's

- Keep diagrams focused on a single concept or layer
- Use consistent naming conventions across all diagrams
- Include legends for symbols and patterns
- Document the purpose and scope of each diagram
- Update diagrams when architecture changes
- Use meaningful labels on relationships and arrows
- Group related entities or components
- Show data flow direction clearly

### Don'ts

- Mix multiple architecture levels in one diagram
- Use ambiguous relationship labels
- Create overly complex diagrams (split if needed)
- Forget to version diagrams with architecture
- Use unexplained abbreviations
- Create diagrams without describing their context
- Mix different diagram types without clear purpose
- Ignore performance implications in flowcharts

## Mermaid Rendering Locations

Mermaid diagrams render in these environments:

- **Markdown files** – GitHub, GitLab, Gitea, Notion, etc.
- **Code documentation** – Within JSDoc, Pydoc comments
- **Confluence** – Via Mermaid plugin
- **Obsidian** – Built-in support
- **VS Code** – Via Markdown preview or extensions
- **Online** – [Mermaid Live Editor](https://mermaid.live)

## Tools and Extensions

- **Mermaid CLI** – Generate diagrams from command line
- **VS Code Extension** – Mermaid extension for syntax highlighting
- **Draw.io Integration** – Export from Mermaid to draw.io
- **Mermaid Preview** – Real-time preview in VS Code

## Resources

- [Official Mermaid Documentation](https://mermaid.js.org)
- [Mermaid Live Editor](https://mermaid.live)
- [Mermaid GitHub Repository](https://github.com/mermaid-js/mermaid)
