class Module:
    def __init__(self, module_id, module_type, version, parameters, mapper=None, metadata=None):
        self.id = module_id
        self.module = module_type
        self.version = version
        self.parameters = parameters
        self.mapper = mapper
        self.metadata = metadata

class Metadata:
    def __init__(self, designer, restore, parameters=None, interface=None):
        self.designer = designer
        self.restore = restore
        self.parameters = parameters
        self.interface = interface

class Designer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Restore:
    def __init__(self, parameters=None, extra=None):
        self.parameters = parameters
        self.extra = extra

class Parameter:
    def __init__(self, name, param_type, label, required=False, spec=None, validate=None):
        self.name = name
        self.type = param_type
        self.label = label
        self.required = required
        self.spec = spec
        self.validate = validate

class Flow:
    def __init__(self, modules, routes=None):
        self.modules = modules
        self.routes = routes

class Router:
    def __init__(self, routes):
        self.routes = routes

class Route:
    def __init__(self, flow):
        self.flow = flow

class AppointmentUpdater:
    def __init__(self, name, flow, metadata):
        self.name = name
        self.flow = Flow(flow)
        self.metadata = metadata

# Define parameters and their specifications
param_hook = Parameter("hook", "hook:gateway-webhook", "Webhook", True)
param_maxResults = Parameter("maxResults", "number", "Maximum number of results")
param_interface_message = Parameter("message", "collection", "Message Interface", spec=[
    Parameter("call", "collection", "Call Specification", spec=[
        Parameter("assistant", "collection", "Assistant Specification", spec=[
            Parameter("firstMessage", "text", "First Message"),
            # Add more parameters as needed
        ])
    ])
])

# Define metadata and designer layout
metadata_module1 = Metadata(
    designer=Designer(x=0, y=0),
    restore=Restore(parameters={"hook": {"data": {"editable": "true"}, "label": "UpdateEventRIki"}}),
    parameters=[param_hook, param_maxResults],
    interface=[param_interface_message]
)

# Define modules
module1 = Module(
    module_id=1,
    module_type="gateway:CustomWebHook",
    version=1,
    parameters={"hook": 499713, "maxResults": 1},
    mapper={},
    metadata=metadata_module1
)

# Continue defining other modules
# ...

# Define the flow with a list of modules
flow_modules = [module1]  # Include other module instances as well

# Define the entire system
appointment_updater = AppointmentUpdater(
    name="Appointment Updater",
    flow=flow_modules,
    metadata=None  # Include metadata as required
)