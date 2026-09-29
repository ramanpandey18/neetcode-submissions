class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()

        route = []
        
        def dfs(airport):
            destinations = graph[airport]
            print(destinations, "\n")
            while destinations:
                next_des = destinations.pop(0)
                dfs(next_des)
            route.append(airport)

        dfs("JFK")
        return route[::-1]


        # Step 1: Build the graph.
        # Each airport maps to a list of destinations you can fly to from it.
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        # Step 2: Sort each airport's destination list alphabetically.
        # This ensures that when we explore, we always try the
        # lexicographically smallest destination first.
        for src in graph:
            graph[src].sort()

        # This will hold our final itinerary, but built in REVERSE order.
        route = []

        def dfs(airport):
            # graph[airport] is the list of unused destinations from this airport.
            destinations = graph[airport]

            # Keep flying out of this airport as long as tickets remain.
            while destinations:
                # Always take the smallest (leftmost, since sorted) destination.
                # pop(0) removes it from the list, "using up" that ticket
                # so we never use the same ticket twice.
                next_dest = destinations.pop(0)

                # Recurse into the next airport BEFORE marking current airport done.
                # This is what makes it post-order / Hierholzer's algorithm.
                dfs(next_dest)

            # Only after ALL outgoing tickets from `airport` are used up
            # do we add it to our route. This guarantees dead-ends get
            # finalized first, ending up at the correct spot once reversed.
            route.append(airport)

        # Step 3: Start the DFS from JFK, as required by the problem.
        dfs("JFK")

        # Step 4: Since we appended airports in "finish order" (post-order),
        # the route is actually backwards. Reverse it to get the real itinerary.
        return route[::-1]


    # Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
    # Graph built:
    # JFK -> [BUF]
    # BUF -> [HOU]
    # HOU -> [SEA]
    # Trace of dfs("JFK"):
    # Call	What happens
    # dfs("JFK")	destinations = ["BUF"], pop "BUF", call dfs("BUF")
    # dfs("BUF")	destinations = ["HOU"], pop "HOU", call dfs("HOU")
    # dfs("HOU")	destinations = ["SEA"], pop "SEA", call dfs("SEA")
    # dfs("SEA")	destinations = [] (empty), while loop doesn't run, append "SEA" → route = ["SEA"]
    # back in dfs("HOU")	no more destinations, append "HOU" → route = ["SEA", "HOU"]
    # back in dfs("BUF")	no more destinations, append "BUF" → route = ["SEA", "HOU", "BUF"]
    # back in dfs("JFK")	no more destinations, append "JFK" → route = ["SEA", "HOU", "BUF", "JFK"]

    # Reverse: ["JFK", "BUF", "HOU", "SEA"] ✅ Matches expected output.


    # The Key Idea: Hierholzer's Algorithm

    # Instead of building the path in the order you visit airports, you add an airport to the result only after you've used up all of its outgoing tickets (post-order). Then you reverse the result at the end.

    # Why this works: Any airport that becomes a "dead end" (no tickets left) gets finalized into the path early — but because we build it in reverse and flip it at the end, those dead ends land in the correct position, at the very end of whatever sub-path led to them. This automatically handles cases where you must dip into a dead-end loop before continuing your main route.