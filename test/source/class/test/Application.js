
qx.Class.define("test.Application", {  extend : qx.application.Standalone
    ,members :    {
        main : function() {
            this.base(arguments);

            if ((qx.core.Environment.get("qx.debug"))) {
                qx.log.appender.Native;
                qx.log.appender.Console;
            }

            var sample = new test.draw.Test();
            var doc = this.getRoot();
            doc.add(sample.getWidget(), {edge: 0});
        }
    }
});

