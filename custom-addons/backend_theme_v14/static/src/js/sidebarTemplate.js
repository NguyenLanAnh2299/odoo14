/* Copyright 2018 Tecnativa - Jairo Llopis
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

odoo.define("sidebarTemplate", function (require) {
    "use strict";
    var Widget = require('web.Widget');

    var SidebarTemplate = Widget.extend({
        template: 'sidebar-template',
        init: function () {
            console.log("1");
            this._super.apply(this, arguments);
        },
        start: function(){
            console.log("1");
        }
    });
    return SidebarTemplate;
});
