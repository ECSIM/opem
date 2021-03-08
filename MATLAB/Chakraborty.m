close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import model
opem = py.importlib.import_module('opem');
model = opem.Dynamic.Chakraborty;
test_vector = opem.Params.Chakraborty_Standard_Vector;

% Model inputs
test_vector{'N0'} = 1; % Number of cells
test_vector{'u'} = 0.8; % Fuel utilization ratio
test_vector{'E0'} = 0.6; % No load voltage [V]
test_vector{'T'} = 1273; % Fuel cell temperature [K]
test_vector{'KH2'} = 0.000843; % Hydrogen valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'KO2'} = 0.00252; % Oxygen valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'KH2O'} = 0.000281; % Water valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'rho'} = 1.145; % Hydrogen-Oxygen flow rate
test_vector{'R'} = 0.00328125; % Internal  ohmic  resistance [ohm]
test_vector{'i-start'} = 0.1; % Cell operating current start point [A]
test_vector{'i-stop'} = 300; % Cell operating current end point [A]
test_vector{'i-step'} = 0.1; % Cell operating current step
test_vector{'Name'} = 'Chakraborty_Test';

% Run simulation
test_mode = true;
print_mode = true;
report_mode = false;
result = model.Dynamic_Analysis(test_vector,test_mode,print_mode,report_mode);

% Model outputs
P = cellfun(@vector_filter, cell(result{'P'}));
I = cellfun(@vector_filter, cell(result{'I'}));
V = cellfun(@vector_filter, cell(result{'V'}));
EFF = cellfun(@vector_filter, cell(result{'EFF'}));
Ph = cellfun(@vector_filter, cell(result{'Ph'}));
VE = cellfun(@vector_filter, cell(result{'VE'}));
PO2 = cellfun(@vector_filter, cell(result{'PO2'}));
PH2 = cellfun(@vector_filter, cell(result{'PH2'}));
PH2O = cellfun(@vector_filter, cell(result{'PH2O'}));
Nernst_Gain = cellfun(@vector_filter, cell(result{'Nernst Gain'}));
Ohmic_Loss = cellfun(@vector_filter, cell(result{'Ohmic Loss'}));

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

% Nernst Gain & Ohmic Loss
figure(3)
plot(I,Nernst_Gain)
xlabel('I(A)')
ylabel('V(V)')
hold on
plot(I,Ohmic_Loss)
legend('Nernst Gain','Ohmic Loss')

% Efficiency
figure(4)
plot(I,EFF)
xlabel('I(A)')
ylabel('EFF')
legend('Efficiency')

% Power-Thermal
figure(5)
plot(I,Ph)
xlabel('I(A)')
ylabel('P(W)')
legend('Power(Thermal)')

% PO2
figure(6)
plot(I,PO2)
xlabel('I(A)')
ylabel('PO2(atm)')
legend('PO2')

% PH2
figure(7)
plot(I,PH2)
xlabel('I(A)')
ylabel('PH2(atm)')
legend('PH2')

% PH2O
figure(8)
plot(I,PH2O)
xlabel('I(A)')
ylabel('PH2O(atm)')
legend('PH2O')

