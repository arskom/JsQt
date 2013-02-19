
qx.Class.define("test.impl.Test", { extend: test.draw.Test
    ,members:  {
        create_lbl_custom: function() {
            var retval = this.base(arguments);
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
