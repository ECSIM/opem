close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import model
opem = py.importlib.import_module('opem');
model = opem.Static.Amphlett;
test_vector = opem.Params.Amphlett_Standard_Vector;

% Model inputs
test_vector{'T'} =  343.15; % Cell operation temperature [K]
test_vector{'PH2'} = 1; % Partial pressure [atm]
test_vector{'PO2'} = 1; % Partial pressure [atm]
test_vector{'i-start'} = 0; % Cell operating current start point [A]
test_vector{'i-stop'} = 75; % Cell operating current end point [A]
test_vector{'i-step'} = 0.1; % Cell operating current step
test_vector{'A'} = 50.6; % Active area [cm^2]
test_vector{'l'} = 0.0178; % Membrane thickness [cm]
test_vector{'lambda'} = 23; % An adjustable parameter with a min value of 14 and max value of 23
test_vector{'N'} = 1; % Number of single cells
test_vector{'R'} = 0; % R-Electronic [ohm] (*Optional)
test_vector{'JMax'} = 1.5; % maximum current density [A/(cm^2)]
test_vector{'B'} = 0.016; % An empirical constant depending on the cell and its operation state (Tafel slope) [V]
test_vector{'Name'} = 'Amphlett_Test';

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
Eta_Active = cellfun(@vector_filter, cell(result{'Eta_Active'}));
Eta_Conc = cellfun(@vector_filter, cell(result{'Eta_Conc'}));
Eta_Ohmic = cellfun(@vector_filter, cell(result{'Eta_Ohmic'}));
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

% Eta-Active , Eta-Conc and Eta-Ohmic
figure(3)
plot(I,Eta_Active)
xlabel('I(A)')
ylabel('V(V)')
hold on
plot(I,Eta_Conc)
hold on
plot(I,Eta_Ohmic)
legend('Eta Active','Eta Conc','Eta Ohmic')

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

