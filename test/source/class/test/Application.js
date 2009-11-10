
qx.Class.define("test.Application", {  extend : qx.application.Standalone
    ,members :    {
        main : function() {
            this.base(arguments);

            if (qx.core.Variant.isSet("qx.debug", "on")) {
                qx.log.appender.Native;
                qx.log.appender.Console;
            }

            var sample = new sample.draw.Add();
            doc.add(sample.getWidget(), {edge: 0});
        }
    }
});
