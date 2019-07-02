close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import model
opem = py.importlib.import_module('opem');
model = opem.Static.Chamberline_Kim;
test_vector = opem.Params.Chamberline_Standard_Vector;

% Model inputs
test_vector{'A'} =  50.0; % Active area [cm^2]
test_vector{'E0'} =  0.982; % Open circuit voltage [V]
test_vector{'b'} =  0.0689; % Tafel's parameter for the oxygen reduction [V]
test_vector{'R'} =  0.328; % Resistance [ohm.cm^2]
test_vector{'m'} = 0.000125; % Diffusion's parameters [V]
test_vector{'n'} = 9.45; % Diffusion's parameters [(A^-1)(cm^2)]
test_vector{'N'} = 1; % Number of single cells
test_vector{'i-start'} = 1; % Cell operating current start point [A]
test_vector{'i-stop'} = 42.5; % Cell operating current end point [A]
test_vector{'i-step'} = 0.1; % Cell operating current step
test_vector{'Name'} = 'Chamberline_Test';

% Run simulation
test_mode = true;
print_mode = true;
report_mode = false;
result = model.Static_Analysis(test_vector,test_mode,print_mode,report_mode);

% Model outputs
P = cellfun(@vector_filter, cell(result{'P'}));
I = cellfun(@vector_filter, cell(result{'I'}));
V = cellfun(@vector_filter, cell(result{'V'}));
EFF = cellfun(@vector_filter, cell(result{'EFF'}));
Ph = cellfun(@vector_filter, cell(result{'Ph'}));
VE = cellfun(@vector_filter, cell(result{'VE'}));


% Power-Stack
figure(1)
plot(I,P)
xlabel('I(A)')
ylabel('P(W)')
legend('Power-Stack')

% Voltage-Stack & Linear Approximation
figure(2)
plot(I,V)
xlabel('I(A)')
ylabel('V(V)')
hold on
plot(I,VE)
legend('Voltage-Stack','Linear-Apx')

% Efficiency
figure(3)
plot(I,EFF)
xlabel('I(A)')
ylabel('EFF')
legend('Efficiency')

% Power-Thermal
figure(4)
plot(I,Ph)
xlabel('I(A)')
ylabel('P(W)')
legend('Power(Thermal)')

