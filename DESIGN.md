# Adaptive Task Scheduler Design

## Overview

Adaptive Task Scheduler is a Python-based productivity system that explores how programming paradigms influence software design.

The project models different task types and uses multiple scheduling strategies to create adaptive task recommendations.

## Design Goals

- Demonstrate object-oriented programming concepts.
- Apply abstraction, encapsulation, inheritance, and polymorphism.
- Explore functional programming techniques for task analysis.
- Create a modular and extensible scheduling system.

## Planned Architecture

The project will contain:

- Task models representing different types of tasks.
- Scheduling strategies for different prioritization methods.
- Analytics using functional programming concepts.
- Storage for saving and loading user data.
- A lightweight reward system.

## Programming Concepts

### Object-Oriented Programming

Tasks will be represented as objects with shared behavior through inheritance.

### Polymorphism

Different task types and scheduling strategies will provide their own implementations of behavior.

The scheduler uses polymorphic behaviour by allowing different task subclasses to define their own responses to common actions. For example, all tasks can be completed using the `complete_task()` method, but `RecurringTask` overrides this behaviour to additionally handle recurring schedules.

### Functional Programming

Functional techniques such as map, filter, and lambda expressions will be used for analytics and data processing.

## Project Design Details

### Subclasses of Task 

I made three subclasses.

Each subclass extends the base Task class with additional attributes and behaviours appropriate to its scheduling model. Deadline tasks dynamically increase in urgency, recurring tasks regenerate according to a repetition interval, and project tasks support incremental progress tracking.

                      Task
                       ▲
      ┌────────────────┼────────────────┐
      │                │                │
DeadlineTask    RecurringTask    ProjectTask
      │                │                │
Hard deadline   Repeat interval   Progress tracking
Increasing       Regenerates      Incremental
urgency          after completion completion

## Design Considerations and Future Improvements

### Optional Task Attributes

The current version of Adaptive Task Scheduler stores common attributes such as deadlines in the base Task class so that all task types share a consistent structure. This simplifies implementation and allows the scheduler to handle different tasks uniformly.

However, some task types may not naturally require every attribute. For example, DeadlineTask benefits from a strict deadline, while RecurringTask may be better represented through repetition frequency and scheduling preferences rather than a fixed deadline. ProjectTask is more flexible, it may or may not require a deadline depending on the user. 

The project is following a simplified design thus all classes has attributes that aren't necessary for their structure but not utilized

A future version could refactor the design by moving specialized attributes into their respective subclasses:

- `DeadlineTask` → deadline information
- `RecurringTask` → repeat frequency and recurrence rules
- `ProjectTask` → progress tracking and milestones

This would create a more flexible architecture while preserving the shared behaviour provided by the base Task class. Currently oversimplified versions showcased.


## Future Design Details (Extra Tidbits)

- Automatic project progress calculated from milestones or subtasks instead of manual percentage updates.
- Calendar integration for scheduling recurring and deadline tasks.
- AI-assisted task prioritization based on workload, deadlines, and user habits.
- Optional gamification features such as experience points, achievements, and a virtual garden that grows as tasks are completed.

Note: Future versions will parse deadlines into date/time objects so urgency can be incorporated into the recommendation score.

Future Improvement: When tasks have equal importance, the scheduler will compare parsed deadline values using Python's datetime module to recommend the most urgent task.

### Project Progress Tracking

In Version 1, project progress is updated manually by the user through the `update_progress()` method. This approach keeps the implementation simple while still allowing long-term tasks to be tracked over multiple work sessions.

A future version of the scheduler could replace manual progress updates with milestone-based tracking. Users would be able to divide a project into smaller milestones and mark each milestone as complete. The scheduler would then automatically calculate the project's completion percentage based on the number of completed milestones.

For example:

Project: Adaptive Task Scheduler

☑ Design
☑ Task Model
☐ Scheduler
☐ Testing
☐ Documentation

Progress: 40% (2 of 5 milestones completed)

This approach would provide a more objective measure of project completion while encouraging users to break large goals into manageable steps.

### User-Customisable Categories

The scheduler is designed to be domain-independent. Rather than hard-coding categories such as "Assignment" or "Meeting" into the class hierarchy, users can organise tasks into their own categories (e.g., Assignments, Homework, Work, Fitness, Chores). The underlying scheduling behaviour remains based on task type (DeadlineTask, RecurringTask, or AnytimeTask), allowing the application to remain flexible for students, professionals, and personal use.

While the scheduler internally classifies tasks by scheduling behaviour (e.g., DeadlineTask, RecurringTask, and AnytimeTask), a future version could allow users to create custom organisational categories such as Assignments, Homework, Meetings, Fitness, or Shopping etc within each (e.g: all these are groups inside DeadlineTask). These categories would improve organisation and navigation without affecting the scheduling algorithm or object-oriented design.

### Scheduled Time Windows

Allow tasks to have an optional preferred start time or time window (e.g., 8:00 AM, 6:00–7:00 PM). Users may keep these times fixed or allow the scheduler to adjust them automatically when generating an optimized daily schedule.

### Routine and Timetable Support

Recurring tasks can be assigned to preferred times of day, enabling users to build consistent daily or weekly routines. This allows the scheduler to function as both a task manager and a personal timetable planner.


### Calendar Integration

Integrate the scheduler with a calendar view so tasks can be visualized by day, week, or month. Scheduled tasks would appear alongside deadlines, helping users balance long-term planning with daily execution.

### Printable Daily Schedule

Generate a clean, printable agenda containing prioritized tasks, scheduled time blocks, estimated durations, and available free time. This would provide users with an easy-to-follow plan for the day.

### Flexible Scheduling

Allow users to choose between fixed schedules and adaptive schedules. Fixed tasks remain locked to their assigned times, while flexible tasks can be automatically rearranged by the scheduler based on priority, urgency, and available time.

### Hybrid Planning System

Combine deadline-driven tasks, recurring routines, and long-term projects into a single unified schedule. This creates a balance between structured commitments and flexible personal goals while preserving the adaptive nature of the scheduler.

### AI-Assisted Scheduling

Integrate AI to provide personalized scheduling recommendations based on user habits, workload, task history, and available time. The system could suggest optimal work sessions, estimate task durations, identify potential scheduling conflicts, and recommend the best task to complete next.

### Intelligent Priority Suggestions

Instead of requiring users to manually assign importance to every task, AI could analyze task names, deadlines, previous behaviour, and scheduling patterns to recommend an appropriate importance level while still allowing manual adjustments.

### Productivity Insights

Generate weekly and monthly productivity reports, highlighting completed tasks, focus trends, recurring bottlenecks, and time allocation across different types of work. These insights could help users refine their planning habits over time.

### Virtual Companion and Garden

Reward consistent productivity with a relaxing virtual environment where plants, flowers, or small companions grow as tasks are completed. The visual progression serves as positive reinforcement without affecting the scheduling algorithm.

### Gamification System

Introduce experience points (XP), achievement badges, streaks, levels, and milestone rewards for completing tasks and maintaining productive routines. Gamification encourages long-term engagement while preserving the application's primary focus on effective scheduling.

### Focus Sessions

Integrate customizable focus timers, such as the Pomodoro Technique or user-defined work intervals. Completing focus sessions could contribute to progress tracking, experience points, and productivity statistics.

### Adaptive Learning

The scheduler could gradually learn from user behaviour, recognizing preferred working hours, realistic task durations, and frequently postponed activities. Over time, scheduling recommendations would become increasingly personalized.

### Cross-Platform Synchronization

Synchronize tasks across desktop, mobile devices, and cloud storage while integrating with popular calendar applications to maintain a consistent scheduling experience.

Note: Scheduler vs Planner vs Routine
