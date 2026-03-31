# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

### Flowchart of the main workflow
```mermaid
    flowchart TD
        A([Start Program]) --> B[Main Menu]
        B --> C{User Input}
        
        C -- "1" --> D[Login as student]
        D --> E{New or StudentID}
        E -- "if new" --> A1[Enter details] --> A2
        E -- "input StudentID" --> A2[New menu]
        A2 --> A3{User Input}
        A3 -- "1" --> A4[View Course Catalog]
        A3 -- "2" --> A5[Register for a Course]
        A3 -- "3" --> A6[Drop a Course]
        A3 -- "4" --> A7[View My Schedule]
        A3 -- "5" --> A8[Billing Summary]
        A3 -- "6" --> A9[Edit My Profile]
        A3 -- "7" --> A10[Logout and Save]
        
        C -- "2" --> F[Login as admin]
        C -- "3" --> L([Exit Program])
        
        C -- "Invalid" --> M[Display Error Message]
        M --> B
```
### Prompts
