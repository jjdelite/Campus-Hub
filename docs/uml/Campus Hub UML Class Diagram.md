# Campus Hub — UML Class Diagram

Following the Week 5 UML lecture (class diagrams, + public / − private / # protected, associations). Built from the actual classes in this repo (planner/models/), labeled in the code as UML CD-1 (Student, Administrator) and CD-2 (Course, Item, RepeatingEvent). Paste the PlantUML into draw.io or Lucidchart to render it.

```plantuml
@startuml CampusHub
class User {
  - username : String
  - email : String
  - password : String (hashed)
  - first_name : String
  - is_staff : Boolean
}

class Student {
  - reminders_on : Boolean
  + getName() : String
  + getEmail() : String
  + getCourses() : List<Course>
  + getItems() : List<Item>
  + getEvents() : List<RepeatingEvent>
  + getUpcomingItems(days : int) : List<Item>
  + getCompletedItems() : List<Item>
  + areRemindersOn() : Boolean
  + setReminders(on : Boolean) : void
}

class Administrator {
  - user : User
  + listStudents() : List<Student>
  + searchStudents(text : String) : List<Student>
  + deleteStudent(student : Student) : void
}

class Course {
  - name : String
  - code : String
  - is_activity : Boolean
  - color : String
  + getName() : String
  + getItems() : List<Item>
  + countItems() : int
  + rename(name : String, code : String) : void
}

class Item {
  - title : String
  - item_type : String
  - due_date : Date
  - due_time : Time
  - end_time : Time
  - location : String
  - notes : String
  - completed : Boolean
  + validate() : void
  + update(changes) : void
  + markComplete() : void
  + markNotDone() : void
  + isCompleted() : Boolean
  + isOverdue() : Boolean
  + kind() : String
}

class ItemType {
  + ASSIGNMENT
  + TEST
  + MEETING
  + JOB_SHIFT
  + CLASS
  + OTHER
}

class RepeatingEvent {
  - title : String
  - item_type : String
  - days_of_week : String
  - start_time : Time
  - end_time : Time
  - first_date : Date
  - last_date : Date
  - location : String
  - skipped_dates : String
  + getDaysList() : List<String>
  + occursOn(day : Date) : Boolean
  + getDatesInWeek(week_start : Date) : List<Date>
  + updateAll(changes) : void
  + deleteOne(day : Date) : void
  + deleteAll() : void
}

User "1" *-- "1" Student : has a (composition)
User "1" <-- "1" Administrator : wraps (staff user)
Student "1" --> "0..*" Course : owns
Student "1" --> "0..*" Item : owns
Student "1" --> "0..*" RepeatingEvent : owns
Course "1" --> "0..*" Item : groups
Course "1" --> "0..*" RepeatingEvent : groups
Item ..> ItemType : typed by
RepeatingEvent ..> ItemType : typed by
@enduml
```

Relationships in words: a Django User has exactly one Student profile (composition); an Administrator is a staff User who can list, search, and delete student accounts (US-12); a Student owns many Courses, Items, and RepeatingEvents; a Course groups many Items and RepeatingEvents (the link is optional); Item and RepeatingEvent are both typed by ItemType.
