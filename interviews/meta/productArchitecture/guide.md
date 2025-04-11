# Product Architecture Guide

## Steps
1. Assumptions and questions
    1. Ask about main features that need to be covered
    2. Ask about non functional requirements 
        - Number of total users
        - Users using the app at the same size 
        - How are users growing? Are they already active or do they grow over time?
        - Storage
        - Limitations
        - Money
    3. Consider edge cases only if really needed
        - What if someone adds a large ammount of data? Should we cover that?
        - Should we consider SQL injection?

2. Database Models
    1. Talk on tradeofs of non relational vs relational databases
    2. Write database information and relations

3. Diagrams of the platform workflow
    1. Start drawing clients (web, mobile, desktop, etc)
        - Web client have almost no limitations on storage and computation
        - Phone client have data limitations. We dont want to waste users data. And we must consider that phones might have slowers speeds because wifi tends to be faster 
    2. If big requests at the same time are made, consider using a load balancer
    3. Consider partitioning servers for certain functionalities like read/write, fetch content, process data, etc. If certain feature is taking more than another, consider having a dedicated server for doing that specific thing
    
4. Create api methods.
    - Here are some examples:
        - `makePost(userId: int, mediaMetadata: List[Media], caption: String, ...)`
        - `likePost(userId: int, postId: int)`
        - `followUser(userId, toFollowId)`
        - `fetchFeed(userId, startTime, deviceClass)`
    - Consider if some methods can be deleted. For example `fetchFeed` could be cached

5. Write features in the design that of the platform could have that could reduce memory, time execution, user experience, etc.
    - For example:
        - Not store media at max resolution, cap it to a maximum
        - Compress files that are not used after x ammount of time
        - Use asyncronous functions to process data while user is doing something else
        - Use pagination to not fetch all information at once, only what is needed/requested

6. Describe key functionalities 
    - Main functionalities need to be highly described
    - Consider if chunks of data can be loaded as requested instead of loading the complete informatiton

7. Write what information can be processed later
    - If there is time to spare, consider functionalities that could be processed later until there is enough time to do it

## Definitions

*Blob*
- Binary Large object 
- To store large files like images, videos, .jars, etc.
- AWS S3, Azure, GCP (Google Cloud Platform), own data center, etc.

*Push model*
- Whenever something happens, a "push" is made and new information is instantly sent to another device/instance.
- Used for live communications like messaging, streaming, videochat, etc.
- Works using web socket
- If lots of things need to be updated at the same time this model is better

*Pull model*
- The device decides certain ammount of time that a pull needs to be done so new information arrive locally.
- Works wit HTTP long polling
- In big ammounts, tends to be more resource intensive
- Better if small ammounts of data need to be updated and there is an action that triggers them (like submit button or refresh)

*Optimistic rendering*
- We can make the render to inform about something even if the backend havent finished the job to do it. 
- Showing the like in a post before it gets written in database
- Make the suer be able to see its photo in profile before it gets fetched in other devices
- Make sent messages to show in conversation before they arrive to its destination  
