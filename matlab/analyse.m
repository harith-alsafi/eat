% define command line arguments 
function []=analyse(inputFile, outputFile)
  % Import the data 
  inputTable = readtable(inputFile);
  
  % Adding new columns and their calculations 
  inputTable.Profit = zeros(height(inputTable), 1);
  inputTable.Ec_Revenue = zeros(height(inputTable), 1);
  inputTable.TotalCost = zeros(height(inputTable), 1);
  inputTable.Profit_Revenue = zeros(height(inputTable), 1);
  inputTable.TotalCost_Revenue = zeros(height(inputTable), 1);
  
  for i=1:height(inputTable)
    inputTable(i, "TotalCost") = inputTable(i, "EnviroemntalCosts") + inputTable(i, "LogisticsCosts") + inputTable(i, "WorkforceCosts")  + inputTable(i, "OtherCosts");
    inputTable(i, "Profit") =  inputTable(i, "Revenue") + inputTable(i, "TotalCost");
    inputTable(i, "Ec_Revenue") = inputTable(i, "EnviroemntalCosts") / inputTable(i, "Revenue");
    inputTable(i, "Profit_Revenue") = inputTable(i, "Profit") / inputTable(i, "Revenue");
    inputTable(i, "TotalCost_Revenue") = inputTable(i, "TotalCost") / inputTable(i, "Revenue");
  end 
  
  % create variables 
  FieldNames = inputTable.Properties.VariableNames;
  MinValues = zeros(length(FieldNames), 1);
  Q1Values = zeros(length(FieldNames), 1);
  Q2Values = zeros(length(FieldNames), 1);
  Q3Values = zeros(length(FieldNames), 1);
  MaxValues = zeros(length(FieldNames), 1);
  Averages = zeros(length(FieldNames), 1);
  Std = zeros(length(FieldNames), 1);
  
  % extracting calculations 
  for i=1:length(FiledNames)
      array = inputTable.(FieldNames(i));
      MinValues(i) = min(array);
      MaxValues(i) = max(array);
      [Q1Values(i), Q2Values(i), Q3Values(i)] = prctile(array, [25, 50, 75]);
      Averages(i) = mean(array);
   dbc.Row([
            dbc.Col(),
            dbc.Col(table.old_table_view),
        ], style={"height":"44vh", 'margin': 10 }, class_name="display: flex; flex-grow: 1;")      Std(i) = std(array);    
  end
  
  % writing data 
  
end