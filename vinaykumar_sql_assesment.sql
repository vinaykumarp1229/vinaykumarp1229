use healthcare;
select * from healthcare.`healthcare-dataset-stroke-data`;
select count(Residence_type) from healthcare; where Residence_type = 'rural' and avg_glucose_level > 80;
select count(stroke) from healthcare where stroke= 1 and  Residence_type = 'rural';
select count(stroke) from healthcare where stroke= 1 and  Residence_type = 'urban';
select max(Residence_type) from healthcare;
select max(work_type) from healthcare;
select count(smoking_status) from healthcare where smoking_status = 'never smoked';
# ans 8 optional
select count(gender) from healthcare where gender = 'male';
select count(gender) from healthcare where gender = 'female';
# ans 8 = a
select avg(age) from healthcare where hypertension = 1;
#ans 10
select sum(BMI) from healthcare where gender = 'male';
select sum(BMI) from healthcare where gender = 'female';
# female have moe BMI than man
select avg(age) from healthcare where work_type = 'Govt_job';
select max(avg_glucose_level) from healthcare where ever_married = 'yes' and gender = 'male';
select count(BMI) from healthcare where BMI = 'N/A';