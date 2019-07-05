close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import model
opem = py.importlib.import_module('opem');
model = opem.Static.Larminie_Dicks;
test_vector = opem.Params.Larminiee_Standard_Vector;

% Model inputs
test_vector{'A'} = 0.0587; % The slope of the Tafel line [V]
test_vector{'E0'} = 1.178; % Fuel cell reversible no loss voltage [V]
test_vector{'B'} =  0.0517; % Constant in the mass transfer term [V]
test_vector{'RM'} = 0.0018; % The membrane and contact resistances [ohm]
test_vector{'i_0'} =  0.00654; % Exchange current at which the overvoltage begins to move from zero [A]
test_vector{'i_L'} = 100.0; % Limiting current [A]
test_vector{'i_n'} = 0.23; % Internal current [A]
test_vector{'N'} = 23; % Number of single cells
test_vector{'i-start'} = 0.1; % Cell operating current start point [A]
test_vector{'i-stop'} = 98; % Cell operating current end point [A]
test_vector{'i-step'} = 0.1; % Cell operating current step
test_vector{'Name'} = 'Larminiee_Test';

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

