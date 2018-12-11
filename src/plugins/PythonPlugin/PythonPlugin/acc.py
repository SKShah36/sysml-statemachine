
import random
import time

class StateMachine:

	def __init__(self):
		self.model = {'Send to airport travel agency': [{'dst': 'Final', 'Type': 'State', 'transition_guard': False, 'trigger': False}], 'Final': [{'dst': 'Final', 'Type': 'Final', 'transition_guard': False, 'trigger': False}], 'Give passengers travel documents': [{'dst': 'Final', 'Type': 'State', 'transition_guard': False, 'trigger': False}], 'Print Boarding Pass': [{'dst': 'Merge3', 'Type': 'State', 'transition_guard': False, 'trigger': False}], 'Choice3': [{'dst': 'Merge3', 'Type': 'Choice', 'transition_guard': False, 'trigger': False}], 'Merge3': [{'dst': 'Give passengers travel documents', 'Type': 'Merge', 'transition_guard': False, 'trigger': False}], 'Initial': [{'dst': 'Verify_Reservation', 'Type': 'Initial', 'transition_guard': False, 'trigger': False}], 'Verify_Reservation': [{'dst': 'Choice1', 'Type': 'State', 'transition_guard': False, 'trigger': False}], 'Choice1': [{'dst': 'Send to airport travel agency', 'Type': 'Choice', 'transition_guard': False, 'trigger': False}, {'dst': 'Get Preferences', 'Type': 'Choice', 'transition_guard': False, 'trigger': False}], 'Get Preferences': [{'dst': 'Fork', 'Type': 'State', 'transition_guard': False, 'trigger': False}], 'Fork': [{'dst': 'Print Boarding Pass', 'Type': 'Fork', 'transition_guard': False, 'trigger': False}, {'dst': 'Choice2', 'Type': 'Fork', 'transition_guard': False, 'trigger': False}], 'Choice2': [{'dst': 'Receive baggage and Print receipts', 'Type': 'Choice', 'transition_guard': False, 'trigger': False}, {'dst': 'Choice3', 'Type': 'Choice', 'transition_guard': 'NoBaggage', 'trigger': 'NoBaggage'}], 'Receive baggage and Print receipts': [{'dst': 'Choice3', 'Type': 'State', 'transition_guard': False, 'trigger': False}]}
		curr_node= 'Initial'
		print('Current_node: {}'.format(curr_node))
		self.run(curr_node)

	def run(self, node):
		self.current_node=node
		current_node=self.current_node
		print('Current node:', current_node)
		merge_nodes=[]

		while True:

			possible_choices = {'State': [], 'Choice': [], 'Fork': [], 'Merge': [], 'Initial': [], 'Final': []}

			trigger_flag=0

			for items in self.model[current_node]:
				if (items['transition_guard'] and items['trigger']):
					trigger_flag=1
					current_node=items['dst']

				else:
					possible_choices[items['Type']].append(items['dst'])
			if trigger_flag==0:
				current_node=random.choice(possible_choices[self.model[current_node][0]['Type']])
			print('Current_node: {}'.format(current_node))

			if self.model[current_node][0]['Type'] == 'State':

				current_state=current_node
				print('Current_state: {}'.format(current_state))
			if self.model[current_node][0]['Type'] == 'Fork':

				for lst in self.model[current_node]:
					self.run(lst['dst'])
					self.run(lst['dst'])
			if self.model[current_node][0]['Type'] == 'Merge':

				merge_nodes.append(current_node)
			if current_node=='Final':
				print('State machine executed. Exiting')
				break
			time.sleep(2)



def main():
	StateMachine()


if __name__ == '__main__':
	main()