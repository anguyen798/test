##
#  Compute the number of reachable people in a social network.
#

def main() :
   # Gather input from the user.
   degree = int(input("Enter the degree: "))
   friends = int(input("Enter the average friends per user: "))

   # Compute the number of reachable people.  Add 1 to include the original 
   # user.
   reachable = reachablePeople(degree, friends) + 1

   # Display the result.
   print(reachable, "people are reachable with those values.")

## Compute the number of reachable people.
#  @param degree the maximum degree of separation
#  @param averageFriendsPerUser the number of friends for each user
#  @returns the number of reachable people
#
def reachablePeople(degree, averageFriendsPerUser) :
   if degree == 0 :
      return 0
   else :
      return averageFriendsPerUser + \
             averageFriendsPerUser * reachablePeople(degree - 1, averageFriendsPerUser)

# Call the main function.
main()

