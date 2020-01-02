/* Copyright 2016 OCA/oscar@vauxoo.com
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define("website_cms.tour", function (require) {
    "use strict";

//    var core = require("web.core");
    var Tour = require("web_tour.tour");
//    var base = require("web_editor.base");
//    var _t = core._t;

     Tour.register("question", {
        url: "/cms/add-page",
        wait_for: base.ready(),
    }, [Tour.STEPS.WEBSITE_NEW_PAGE,
            {
                title: "Fill form with the data to create the 'Demo Page'",
                element: "button.btn-primary:contains(Submit)",
                onload: function () {
                    $('input[name="name"]').val('Demo Page');
                    $('textarea[name="description"]').val('Demo Page Description');
                    $('input.select2-input.select2-default').val('TestTag');
                },
            },

            {
        trigger: ".select2-choices",
        extra_trigger: ".note-editable p:not(:containsExact(\"<br>\"))",
        content: _t("Insert tags related to your question."),
        position: "top",
        run: function (actions) {
            actions.auto("input[id=s2id_autogen2]");
        },
    },
            {
                title: "Wait for the page editor to be displayed",
                waitFor: "div:contains(Insert Blocks)",
                element: "a:contains(Discard)",
            },
            {
                title: "Click on 'Metadata' link in order to edit the page created",
                waitFor: "li.edit.edit-frontend.ml16:contains(Metadata)",
                element: "a:contains(Metadata)",
            },
            {
                title: "Edit the page",
                waitFor: "h2:contains(Edit page)",
                element: "button.btn-primary:contains(Submit)",
                onload: function () {
                    $('input[name="name"]').val('Demo Page edited');
                    $('textarea[name="description"]').val('Demo Page Description Edited');
                    $('input.select2-input.select2-default').val('TestTagEdited');
                },
            },
            {
                title: "Wait for the success message of page edition",
                waitFor: "div.alert.alert-info.alert-dismissible:contains(Page updated.)",
            },

        ]);


});
