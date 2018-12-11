"""
This is where the implementation of the plugin code goes.
The MyPythonPlugin-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('MyPythonPlugin')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class MyPythonPlugin(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    META = {}
    METANodes = core.get_all_meta_nodes(active_node)
    for path in METANodes:
      node = METANodes[path]
      META[core.get_attribute(node,'name')] = node
    
    children = core.load_children(active_node)
    self.model = {'name':core.get_attribute(active_node,'name'),'components':[],'connections':[]}
    
    for child in children:
      if core.is_type_of(child,META['Component']):
        self.process_component(child)
      else:
        self.process_connection(child)
    
    logger.info(self.get_code())
    self.save_code()
    
  def process_component(self, node):
    self.model['components'].append({'URI':self.core.get_attribute(node,'ModelicaURI'),'name':self.core.get_attribute(node,'name')})
  
  def process_connection(self, node):
    src = self.core.load_pointer(node,'src')
    dst = self.core.load_pointer(node,'dst')
    item = {'src':'','dst':''}
    item['src'] = self.core.get_attribute(self.core.get_parent(src),'name') + '.' + self.core.get_attribute(src,'name')
    item['dst'] = self.core.get_attribute(self.core.get_parent(dst),'name') + '.' + self.core.get_attribute(dst,'name')
    self.model['connections'].append(item);
  
  def get_code(self):
    code_text = '\n'
    code_text += 'model ' + self.model['name'] + '\n'
    for component in self.model['components']:
      code_text += '  ' + component['URI'] + ' ' + component['name'] + ';\n'
    code_text += 'equation\n'
    for connection in self.model['connections']:
      code_text += '  connect(' + connection['src'] + ', ' + connection['dst'] + ');\n'
    code_text += 'end ' + self.model['name'] + '\n';
    
    return code_text;
  
  def save_code(self):
    self.add_file('mod_code_'+self.model['name']+'.mo',self.get_code())
