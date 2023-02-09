##
#  Demonstrate the voting machine class.
#
from voting_machine import VotingMachine

# Create a new voting machine.
vm = VotingMachine()

# Cast 7 votes.
vm.voteDemocrat()
vm.voteDemocrat()
vm.voteRepublican()
vm.voteDemocrat()
vm.voteRepublican()
vm.voteDemocrat()
vm.voteRepublican()

# Show the vote tallies.
print("Democrats: %d    Republicans: %d" % vm.getTallies())

