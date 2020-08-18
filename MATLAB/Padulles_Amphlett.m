close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import model
opem = py.importlib.import_module('opem');
model = opem.Dynamic.Padulles_Amphlett;
test_vector = opem.Params.Padulles_Amphlett_Standard_Vector;

% Model inputs
test_vector{'A'} = 50.6; % Active area [cm^2]
test_vector{'l'} = 0.0178; % Membrane thickness [cm]
test_vector{'lambda'} = 23; % An adjustable parameter with a min value of 14 and max value of 23
test_vector{'JMax'} = 1.5; % Maximum current density [A/(cm^2)]
test_vector{'T'} = 343; % Fuel cell temperature [K]
test_vector{'N0'} = 5; % No load voltage [V]
test_vector{'KO2'} = 0.0000211; % Oxygen valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'KH2'} = 0.0000422; % Hydrogen valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'KH2O'} = 0.000007716; % Water valve constant [kmol.s^(-1).atm^(-1)]
test_vector{'tH2'} = 3.37; % Hydrogen time constant [s]
test_vector{'tO2'} = 6.74; % Oxygen time constant [s]
test_vector{'t1'} = 2; % Reformer time constant [s]
test_vector{'t2'} = 2; % Reformer time constant [s]
test_vector{'tH2O'} = 18.418; % Water time constant [s]
test_vector{'rho'} = 1.168; % Hydrogen-Oxygen flow rate
test_vector{'qMethanol'} = 0.0002; % Molar flow of methanol [kmol.s^(-1)]
test_vector{'CV'} = 2; % Conversion factor
test_vector{'i-start'} = 0.1; % Cell operating current start point [A]
test_vector{'i-stop'} = 75; % Cell operating current end point [A]
test_vector{'i-step'} = 0.1; % Cell operating current step
test_vector{'Name'} = 'Padulles_Amphlett_Test';

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
Eta_Active = cellfun(@vector_filter, cell(result{'Eta_Active'}));
Eta_Conc = cellfun(@vector_filter, cell(result{'Eta_Conc'}));
Eta_Ohmic = cellfun(@vector_filter, cell(result{'Eta_Ohmic'}));

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

% PO2
figure(5)
plot(I,PO2)
xlabel('I(A)')
ylabel('PO2(atm)')
legend('PO2')

% PH2
figure(6)
plot(I,PH2)
xlabel('I(A)')
ylabel('PH2(atm)')
legend('PH2')

% PH2O
figure(7)
plot(I,PH2O)
xlabel('I(A)')
ylabel('PH2O(atm)')
legend('PH2O')

% Eta-Active , Eta-Conc and Eta-Ohmic
figure(8)
plot(I,Eta_Active)
xlabel('I(A)')
ylabel('V(V)')
hold on
plot(I,Eta_Conc)
hold on
plot(I,Eta_Ohmic)
legend('Eta Active','Eta Conc','Eta Ohmic')

