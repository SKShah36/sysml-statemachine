/*globals define*/
/*eslint-env node, browser*/

/**
 * Generated by PluginGenerator 2.20.5 from webgme on Wed Nov 21 2018 14:46:06 GMT-0600 (CST).
 * A plugin that inherits from the PluginBase. To see source code documentation about available
 * properties and methods visit %host%/docs/source/PluginBase.html.
 */

define([
    'plugin/PluginConfig',
    'text!./metadata.json',
    'plugin/PluginBase'
], function (
    PluginConfig,
    pluginMetadata,
    PluginBase) {
    'use strict';

    pluginMetadata = JSON.parse(pluginMetadata);

    /**
     * Initializes a new instance of TutorialPlugin.
     * @class
     * @augments {PluginBase}
     * @classdesc This class represents the plugin TutorialPlugin.
     * @constructor
     */
    function TutorialPlugin() {
        // Call base class' constructor.
        PluginBase.call(this);
        this.pluginMetadata = pluginMetadata;
    }

    /**
     * Metadata associated with the plugin. Contains id, name, version, description, icon, configStructure etc.
     * This is also available at the instance at this.pluginMetadata.
     * @type {object}
     */
    TutorialPlugin.metadata = pluginMetadata;

    // Prototypical inheritance from PluginBase.
    TutorialPlugin.prototype = Object.create(PluginBase.prototype);
    TutorialPlugin.prototype.constructor = TutorialPlugin;

    /**
     * Main function for the plugin to execute. This will perform the execution.
     * Notes:
     * - Always log with the provided logger.[error,warning,info,debug].
     * - Do NOT put any user interaction logic UI, etc. inside this method.
     * - callback always has to be called even if error happened.
     *
     * @param {function(Error|null, plugin.PluginResult)} callback - the result callback
     */
    TutorialPlugin.prototype.main = function (callback) {
        // Use this to access core, project, result, logger etc from PluginBase.

        // Using the logger.
        this.logger.debug('This is a debug message.');
        this.logger.info('This is an info message.');
        this.logger.warn('This is a warning message.');
        this.logger.error('This is an error message.');

        // Using the coreAPI to make changes.
        this.core.setAttribute(nodeObject, 'name', 'My new obj');
        this.core.setRegistry(nodeObject, 'position', {x: 70, y: 70});


        // This will save the changes. If you don't want to save;
        // exclude self.save and call callback directly from this scope.
        this.save('TutorialPlugin updated model.')
            .then(() => {
                this.result.setSuccess(true);
                callback(null, self.result);
            })
            .catch((err) => {
                // Result success is false at invocation.
                this.logger.error(err.stack);
                callback(err, self.result);
            });
    };

    return TutorialPlugin;
});
