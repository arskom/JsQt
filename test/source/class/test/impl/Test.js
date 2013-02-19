
qx.Class.define("test.impl.Test", { extend: test.draw.Test
    ,members:  {
        /*
         * the same create_lbl_custom function is defined the draw class.
         * you must change this function's name when you change the widget
         * name in the .ui file.
         */
        create_lbl_custom: function() {
            var retval = this.base(arguments);

            // JsQt doesn't translate the wrap property from Qt Designer.
            // Here's the workaround for it. Patches are welcome!
            retval.setWrap(true);
            retval.setRich(true);

            return retval;
        }

        ,create_btn_custom: function() {
            var retval = this.base(arguments);

            retval.addListener('execute', this.__on_btn_custom_execute, this);

            return retval;
        }

        ,__on_btn_custom_execute: function(e) {
            alert("Hello world! Here's an unhelpful representation of the " +
                  "event object: " + e);
        }
    }
});
