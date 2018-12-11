"""
This is where the implementation of the plugin code goes.
The PythonPlugin-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('PythonPlugin')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PythonPlugin(PluginBase):

    def main(self):
        core = self.core
        root_node = self.root_node
        active_node = self.active_node

        self.meta={}

        METANodes=self.core.get_all_meta_nodes(active_node)

        for path in METANodes:
            node = METANodes[path]
            self.meta[core.get_attribute(node, 'name')] = node


        children = core.load_children(active_node)

        self.trans=[]
        self.states=[]
        self.state_trans={}
        self.model = {'name': core.get_attribute(active_node, 'name'), 'State': [], 'Transition': []}

        self.active_node_name=core.get_attribute(active_node, 'name')

        self.name_type={}

        #self.model = {core.get_attribute(self.core.get_base_type(self.active_node), 'name'): core.get_attribute(active_node, 'name'), 'State': [], 'Transition': {'src-dst_pair': [],core.get_attribute(self.active_node,'name'): }}

        for child in children:
            self.name_type[self.core.get_attribute(child, 'name')] = self.core.get_attribute(self.core.get_meta_type(child), 'name')
            if core.is_type_of(child, self.meta['State']):
                self.process_state(child)
                self.states.append(self.core.get_attribute(child, 'name'))

            elif core.is_type_of(child, self.meta['Transition']):
                self.process_transition(child)
        self.srclist=[]
        for chd in children:

            src_name=''
            if core.is_type_of(chd, self.meta['Transition']):
                src = self.core.load_pointer(chd, 'src')
                dst = self.core.load_pointer(chd, 'dst')
                src_name = self.core.get_attribute(src, 'name')
                dst_name = self.core.get_attribute(dst, 'name')
                guard=self.core.get_attribute(chd, 'Guard')
                trigger=guard=self.core.get_attribute(chd, 'Trigger')


            if src_name in self.name_type.keys():
                if src_name not in self.state_trans.keys():
                    self.state_trans[src_name]=[]
                self.state_trans[src_name].append({'dst': dst_name, 'Type': self.name_type[src_name],'transition_guard': guard, 'trigger': trigger})
                if self.name_type[dst_name]=='Final':
                    self.state_trans[dst_name] = []
                    self.state_trans[dst_name].append({'dst': dst_name, 'Type': self.name_type[dst_name],'transition_guard': guard, 'trigger': trigger})



        name = core.get_attribute(active_node, 'name')

        logger.info('ActiveNode at "{0}" has name {1}'.format(core.get_path(active_node), name))

        commit_info = self.util.save(root_node, self.commit_hash, 'master', 'Python plugin updated the model')
        logger.info('committed :{0}'.format(commit_info))
        self.save_code()

    def process_state(self, node):
        self.model['State'].append({'name': self.core.get_attribute(node, 'name')})

    def process_transition(self, node):
        src = self.core.load_pointer(node, 'src')
        dst = self.core.load_pointer(node, 'dst')
        item = dict()
        item['src'] = self.core.get_attribute(src, 'name')
        item['dst'] = self.core.get_attribute(dst, 'name')

        self.model['Transition'].append(item)
        self.trans.append(item)

    def get_code(self):
        code_text = '\n'
        code_text += self.core.get_attribute(self.active_node, 'name')
        code_text += self.core.get_path(self.active_node)
        code_text += '\n All meta nodes{}'.format(self.core.get_all_meta_nodes(self.active_node))
        code_text += '\n Get base type of active node{}'.format(self.core.get_base_type(self.active_node))
        code_text += '\n Get name of the metanode {}'.format(self.core.get_attribute(self.core.get_base_type(self.active_node), 'name'))
        code_text += '\n Children {}'.format(self.core.load_children(self.active_node))
        code_text += '\n META {}\n'.format(self.meta)
        code_text += '\n model {}\n'.format(self.model)
        code_text += '\n state_trans {}\n'.format(self.state_trans)
        code_text += '\n Transitions {}\n'.format(self.trans)
        code_text += '\n States {}\n'.format(self.states)
        code_text += '\n name_type keys {}\n'.format(self.name_type.keys())
        code_text += '\n src list {}\n'.format(self.srclist)

        return code_text

    def exec_code(self):
        code_text ="\n"
        code_text += "import random\n"
        code_text += "import time\n"
        code_text += "\n"
        code_text += "class StateMachine:\n"
        code_text += "\n"
        code_text += "\tdef __init__(self):\n"
        code_text += "\t\tself.model = {}\n".format(self.state_trans)
        code_text += "\t\tcurr_node= 'Initial'\n"
        code_text += "\t\tprint('Current_node: {}'.format(curr_node))\n"
        code_text += "\t\tself.run(curr_node)\n\n"
        code_text += "\tdef run(self, node):\n"
        code_text += "\t\tself.current_node=node\n"
        code_text += "\t\tcurrent_node=self.current_node\n"
        code_text += "\t\tprint('Current node:', current_node)\n"
        code_text += "\t\tmerge_nodes=[]\n\n"
        code_text += "\t\twhile True:\n"
        code_text += "\n"
        code_text += "\t\t\tpossible_choices = {'State': [], 'Choice': [], 'Fork': [], 'Merge': [], 'Initial': [], 'Final': []}\n"
        code_text += "\n"
        code_text += "\t\t\ttrigger_flag=0\n"
        code_text += "\n"
        code_text += "\t\t\tfor items in self.model[current_node]:\n"
        code_text += "\t\t\t\tif (items['transition_guard'] and items['trigger']):\n"
        code_text += "\t\t\t\t\ttrigger_flag=1\n"
        code_text += "\t\t\t\t\tcurrent_node=items['dst']\n"
        code_text += "\n"
        code_text += "\t\t\t\telse:\n"
        code_text += "\t\t\t\t\tpossible_choices[items['Type']].append(items['dst'])\n"
        code_text += "\t\t\tif trigger_flag==0:\n"
        code_text += "\t\t\t\tcurrent_node=random.choice(possible_choices[self.model[current_node][0]['Type']])\n"
        code_text += "\t\t\tprint('Current_node: {}'.format(current_node))\n"
        code_text += "\n"
        code_text += "\t\t\tif self.model[current_node][0]['Type'] == 'State':\n\n"
        code_text += "\t\t\t\tcurrent_state=current_node\n"
        code_text += "\t\t\t\tprint('Current_state: {}'.format(current_state))\n"
        code_text += "\t\t\tif self.model[current_node][0]['Type'] == 'Fork':\n\n"
        code_text += "\t\t\t\tfor lst in self.model[current_node]:\n"
        code_text += "\t\t\t\t\tself.run(lst['dst'])\n"
        code_text += "\t\t\t\t\tself.run(lst['dst'])\n"
        code_text += "\t\t\tif self.model[current_node][0]['Type'] == 'Merge':\n\n"
        code_text += "\t\t\t\tmerge_nodes.append(current_node)\n"
        code_text += "\t\t\tif current_node=='Final':\n"
        code_text += "\t\t\t\tprint('State machine executed. Exiting')\n"
        code_text += "\t\t\t\tbreak\n"
        code_text += "\t\t\ttime.sleep(2)\n"
        code_text += "\n\n"
        code_text += "\n"
        code_text += "def main():\n"
        code_text += "\tStateMachine()\n"
        code_text += "\n"
        code_text += "\n"
        code_text += "if __name__ == '__main__':\n"
        code_text += "\tmain()\n"

        return code_text

    def save_code(self):

        self.add_file('{}.py'.format(self.active_node_name), self.exec_code())

