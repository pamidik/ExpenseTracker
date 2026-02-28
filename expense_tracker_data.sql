--
-- PostgreSQL database dump
--

\restrict 7RD3CAeQKx5xGvg8ADNFmKL5Kh21QRr6rn8Myej64l0paZ4QipwWkTysoBpAkDW

-- Dumped from database version 15.17 (Homebrew)
-- Dumped by pg_dump version 15.17 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categories (id, name, created_at) VALUES (1, 'Food & Dining', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (2, 'Transportation', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (3, 'Shopping', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (4, 'Entertainment', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (5, 'Bills & Utilities', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (6, 'Healthcare', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (7, 'Education', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (8, 'Housing', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (9, 'Insurance', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (10, 'Investment', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (11, 'Other', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (12, 'Income', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (13, 'AutoLoan', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (14, 'House Expenses', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (15, 'India Transfer', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (16, 'Travel', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (17, 'Auto Insurance', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (18, 'CarTagRenewal', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (19, 'HouseMaintenance', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (20, 'TaxRefund', '2026-02-28 08:32:26.740197');
INSERT INTO public.categories (id, name, created_at) VALUES (21, 'MortgageRefund', '2026-02-28 08:32:26.740197');


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203161977, '2026-02-13', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203232484, '2026-02-12', 'March Mortgage Payment', 4900.00, 'Housing', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203299743, '2026-02-06', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203329471, '2026-02-20', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203407051, '2026-02-06', 'February Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203434755, '2026-02-06', 'February Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203624549, '2026-02-27', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203734359, '2026-02-06', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203781585, '2026-02-12', 'Prajwal Birthday Expense', 1650.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771203953007, '2026-02-20', 'India Transfer (30L + 5L Chit Fund)', 1500.00, 'India Transfer', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771204176433, '2026-02-27', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281543521, '2026-01-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281625606, '2026-01-09', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281665710, '2026-01-30', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281699997, '2026-01-23', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281911524, '2026-01-31', 'Refund from MrCooper', 495.00, 'MortgageRefund', 'AdditionalIncome', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281966256, '2026-01-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771281998604, '2026-01-23', 'India Transfer (30L + 5L Chit Fund)', 1620.00, 'India Transfer', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282055923, '2026-01-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282204621, '2026-01-09', 'January Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282224894, '2026-01-09', 'January Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282396677, '2026-01-09', 'Flight Tickets for Amma & Nanna', 2176.00, 'Travel', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282424686, '2026-01-31', 'HOA Payment', 810.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282585235, '2026-01-15', 'Flight Tickets to Omaha', 633.00, 'Travel', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771282616202, '2026-01-24', 'TurboTax Fee - Tax Filing for FY2025', 112.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771283605519, '2026-03-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771283639565, '2026-03-06', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398197, '2026-03-31', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398198, '2026-03-20', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398199, '2026-03-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398200, '2026-03-20', 'India Transfer (30L + 5L Chit Fund)', 1500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398201, '2026-03-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398202, '2026-03-06', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398203, '2026-03-06', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398204, '2026-03-31', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398205, '2026-04-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398206, '2026-04-03', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398207, '2026-04-30', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398208, '2026-04-17', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398209, '2026-04-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398210, '2026-04-17', 'India Transfer (30L + 5L Chit Fund)', 1500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398211, '2026-04-30', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398212, '2026-04-03', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398213, '2026-04-03', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398214, '2026-04-30', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398215, '2026-04-11', 'Madhavi Vadina House Warming Gift', 500.00, 'Other', 'OptionalExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398216, '2026-04-30', 'Visitor Insurance for Amma & Nanna', 2100.00, 'Other', 'OptionalExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398217, '2026-05-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398218, '2026-05-01', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398219, '2026-05-29', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398220, '2026-05-15', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398221, '2026-05-29', 'Divya 3rd Pay Check @ Polaris', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398222, '2026-05-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398223, '2026-05-15', 'India Transfer (30L + 5L Chit Fund)', 1500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398224, '2026-05-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398225, '2026-05-01', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398227, '2026-05-01', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398228, '2026-05-31', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398229, '2026-06-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398230, '2026-06-12', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398231, '2026-06-30', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398232, '2026-06-26', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398233, '2026-06-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398234, '2026-06-26', 'India Transfer (30L + 5L Chit Fund)', 1500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398235, '2026-06-30', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398236, '2026-06-12', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398237, '2026-06-12', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398238, '2026-06-30', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398239, '2026-06-18', 'Car Insurance Renewal (Every 6 Months)', 3000.00, 'Auto Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398240, '2026-06-26', 'LIC Policy @ Krishna (Every 6 Months)', 350.00, 'Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398241, '2026-06-26', 'LIC Policy @ Divya (Every 6 Months)', 350.00, 'Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398242, '2026-07-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398243, '2026-07-10', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398244, '2026-07-31', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398245, '2026-07-24', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398246, '2026-07-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398247, '2026-07-24', 'India Transfer (5L Chit Fund)', 500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398248, '2026-07-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398249, '2026-07-10', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398250, '2026-07-10', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398251, '2026-07-31', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398252, '2026-07-15', 'Ammamma Function', 1000.00, 'Other', 'OptionalExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398253, '2026-08-14', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398254, '2026-08-07', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398256, '2026-08-31', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398257, '2026-08-21', 'Divya 2nd Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398258, '2026-08-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398259, '2026-08-21', 'India Transfer (5L Chit Fund)', 500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398260, '2026-08-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398261, '2026-08-07', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398262, '2026-08-07', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398263, '2026-08-31', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398264, '2026-08-28', 'Divya Vratham', 500.00, 'Other', 'OptionalExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398265, '2026-08-31', 'Max Life Insurance Policy (1L @ September)', 1150.00, 'Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398266, '2026-09-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398267, '2026-09-30', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398268, '2026-09-04', 'Divya 1st Pay Check @ Polaris - 2026', 3379.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398269, '2026-09-15', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398270, '2026-09-30', 'India Transfer (5L Chit Fund)', 500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398271, '2026-09-30', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398272, '2026-09-04', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398273, '2026-09-04', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398274, '2026-09-30', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398275, '2026-10-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398276, '2026-10-30', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398277, '2026-10-30', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398278, '2026-10-30', 'India Transfer (5L Chit Fund)', 500.00, 'India Transfer', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398279, '2026-10-30', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398280, '2026-10-15', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398281, '2026-10-15', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398283, '2026-10-30', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398284, '2026-11-13', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398285, '2026-11-27', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398286, '2026-11-27', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398288, '2026-11-30', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398289, '2026-11-13', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398290, '2026-11-13', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398291, '2026-11-30', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398292, '2026-12-15', 'Krishna 1st Pay Check @ ICE - 2026', 3175.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398293, '2026-12-31', 'Krishna 2nd Pay Check @ ICE - 2026', 3150.00, 'Income', 'PayCheck', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398294, '2026-12-31', 'Home Loan', 4900.00, 'Housing', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398296, '2026-12-31', 'House Expenses (Utilities, Groceries, etc...)', 1500.00, 'House Expenses', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398297, '2026-12-15', 'Toyota Auto Loan', 933.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398298, '2026-12-15', 'Tesla Auto Loan', 789.00, 'AutoLoan', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398299, '2026-12-31', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398300, '2026-12-18', 'Car Insurance Renewal (Every 6 Months)', 3000.00, 'Auto Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398301, '2026-12-31', 'LIC Policy @ Krishna (Every 6 Months)', 350.00, 'Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398302, '2026-12-31', 'LIC Policy @ Divya (Every 6 Months)', 350.00, 'Insurance', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771284398303, '2026-12-31', 'Car Registration Renewals (Every Year)', 300.00, 'CarTagRenewal', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771288942044, '2026-02-15', 'Dollars Sent to Amma & Nanna', 200.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771290995609, '2026-02-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291040972, '2026-03-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291383322, '2026-04-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291399255, '2026-05-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291418829, '2026-06-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291506737, '2026-07-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291521868, '2026-08-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291538971, '2026-09-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291570755, '2026-10-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291585037, '2026-11-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771291601619, '2026-12-13', 'Prajwal Dental Treatment', 302.00, 'Healthcare', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292564435, '2026-03-31', '2025 Tax year Federal Refund', 1776.00, 'TaxRefund', 'AdditionalIncome', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292591595, '2026-03-31', '2025 Tax year Georgia Refund', 1634.00, 'TaxRefund', 'AdditionalIncome', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292707924, '2026-01-01', 'Kiddie Academy Daycare Fee', 160.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292722725, '2026-02-01', 'Kiddie Academy Daycare Fee', 160.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292737273, '2026-03-01', 'Kiddie Academy Daycare Fee', 160.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292750734, '2026-04-01', 'Kiddie Academy Daycare Fee', 160.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292766042, '2026-05-01', 'Kiddie Academy Daycare Fee', 160.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771292951664, '2026-01-31', 'Cabinets Installation - HomeDepot & Lowes ', 600.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293316245, '2026-01-09', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293331481, '2026-01-16', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293344193, '2026-01-23', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293363981, '2026-01-30', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293399160, '2026-02-16', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293413346, '2026-02-06', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771293518903, '2026-01-02', 'APS Training - Prajwal', 85.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771295286575, '2026-02-10', 'Turf Master Lawn Care ', 59.00, 'HouseMaintenance', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771295415542, '2026-01-12', 'Turf Masters Lawn Care', 59.00, 'HouseMaintenance', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771296356542, '2026-03-06', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771296371136, '2026-03-13', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771296387291, '2026-03-20', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771296404642, '2026-03-27', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Scheduled', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771296696075, '2026-02-12', 'TurboTax Fee - Tax Filing for FY2025', 64.00, 'Other', 'OptionalExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1771327579632, '2026-02-25', 'Prajwal Swimming Classes', 40.00, 'Education', 'MandatoryExpense', 'Done', '2026-02-28 08:32:26.740197');
INSERT INTO public.transactions (id, date, description, amount, category, type, status, created_at) VALUES (1772062692067, '2026-02-24', 'Chase New Checking account Bonus', 300.00, 'Income', 'AdditionalIncome', 'Done', '2026-02-28 08:32:26.740197');


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 21, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 7RD3CAeQKx5xGvg8ADNFmKL5Kh21QRr6rn8Myej64l0paZ4QipwWkTysoBpAkDW

