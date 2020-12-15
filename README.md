# SNHUPortfolio

•	Briefly summarize The Gaming Room client and their software requirements. Who was the client? What type of software did they want you to design?

The Gaming Room client was hopeful game development team that tasked us with porting their Android only game, Draw-It-Or-Lose it to a web-app game on Mac, Windows, Linux browsers and IOS platforms. They wanted a seamless cross-platform experience in a Drawing Based Guessing game that users could type the answers to in real time, across different game room instances. Thus the software requirements included cross-platform compatibility, proper load balancing, caching, user authentication with a RESTful api, a database server, and a fileserver (possibly through AWS) for the images.

•	What did you do particularly well in developing this documentation?

I gave the users a lot of different options between Linux, Mac, and Windows platforms to choose from, and I tried to give as little bias as possible to co-align with the dev’s goals (even though I prefer Linux, I recommended a Mac server because of the IOS constraint).

•	What about the process of working through a design document did you find helpful when developing the code?

It helped organize my thoughts when I was forming the hierarchical classes, the UML diagram was helpful in realizing the Singleton and Iterator patterns.

•	If you could choose one part of your work on these documents to revise, what would you pick? How would you improve it?

I might update the Design constraints, given the new server constraints to take into consideration for security if using a serverless function and an AWS fileserver.

•	How did you interpret the user’s needs and implement them into your software design? Why is it so important to consider the user’s needs when designing?

Because of the user’s requirement of cross-compatibility, I opted for a React-native-web team because it would be easier to port the logic between web and portable interfaces, meaning less work. I recommended a Mac server because of the memory analyzing tools and Apple SDK required for testing builds which is essential in the build process. When designing a large scale app that can scale, it’s important that all of the user’s needs are taken into consideration and are scalable and feasible given the constraints. This is because the user has entrusted us with the design decision for their project.

•	How did you approach designing software? What techniques or strategies would you use in the future to analyze and design a similar software application?

In the future I would use a UML approach for large scale projects, and I would incorporate memory analyzing techniques, RESTful API, and invest in a Digital Ocean droplet to start testing my own server configurations for personal web apps.
