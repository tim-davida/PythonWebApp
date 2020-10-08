/*
    Создание базы данных "HardwareListDB"
*/
CREATE DATABASE HardwareListDB
CHARACTER SET utf8
COLLATE utf8_unicode_ci;


/*
    Таблица "Типы оборудования"
*/
CREATE TABLE HardwareTypes (
    TypeId     INT AUTO_INCREMENT NOT NULL UNIQUE,
    TypeName   VARCHAR(48) NOT NULL UNIQUE,
    SerialMask VARCHAR(16),
    PRIMARY KEY (TypeId)
); 


/*
    Таблица "Оборудование"
*/
CREATE TABLE Hardware (
    HardwareId INT AUTO_INCREMENT NOT NULL UNIQUE,
    TypeId     INT NOT NULL,
    SerialNum  VARCHAR(16) NOT NULL UNIQUE,
    PRIMARY KEY (HardwareId),
    FOREIGN KEY (TypeId) REFERENCES HardwareTypes(TypeId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


/*
    Добавление списка типов оборудования
*/
INSERT INTO HardwareTypes (TypeId, TypeName, SerialMask) VALUES
('1',  'Wi-Fi адаптер D-Link DWA-121/B1A',     'NaNAXZaZZaAXZ'),
('2',  'Wi-Fi адаптер D-Link DWA-131/E',       'aZZNaZAaXaZNAXXA'),
('3',  'Wi-Fi адаптер D-Link DWA-137/A1A',     'NANNaAXaaXAaaZX'),
('4',  'Wi-Fi адаптер TP-LINK TL-WN725N',      'XNNAaAaXNZZNAX'),
('5',  'Wi-Fi адаптер TP-LINK TL-WN727N',      'NNZaaXAZAXNXZ'),
('6',  'Wi-Fi адаптер TP-LINK TL-WN781ND',     'ZZNNXXXAaNXXZN'),
('7',  'Wi-Fi адаптер TP-LINK TL-WN821N',      'ZAaNXaZaNaX'),
('8',  'Точка доступа D-Link DAP-1360U',       'ZZXXaXAXXa'),
('9',  'Точка доступа D-Link DAP-3310/RU/A1A', 'AXaZaaXXXZ'),
('10', 'Wi-Fi роутер D-Link DIR-615S',         'NXZNaaNXXaA'),
('11', 'Wi-Fi роутер D-Link DIR-615/T4',       'AaNAZNNaNaN'),
('12', 'Wi-Fi роутер D-Link DIR-620S',         'AAXZZXZNZZ'),
('13', 'Wi-Fi роутер Tenda AC10U',             'NaXAAZXNXaXNNZ'),
('14', 'Wi-Fi роутер Tenda AC1200',            'XNaAXXXAANXANaX'),
('15', 'Wi-Fi роутер Tenda AC15',              'XAXAXANXZAXAXX'),
('16', 'Wi-Fi роутер Tenda AC5',               'NZNNNaANAXZ'),
('17', 'Wi-Fi роутер TP-LINK Archer A9',       'AXaaNZaXZAaZAN'),
('18', 'Wi-Fi роутер TP-LINK Archer AX20',     'aZaAaNaANZXXa'),
('19', 'Wi-Fi роутер TP-LINK Archer C1200',    'NNZXaXaZXAA'),
('20', 'Wi-Fi роутер TP-LINK Archer C2300 v2', 'NAXXXNaNNZAXX'),
('21', 'Роутер TP-LINK M7200',                 'XXANNXAZAXaXN'),
('22', 'Роутер TP-LINK TL-MR150',              'ZXaZANXZNAXANN'),
('23', 'Роутер TP-LINK TL-MR6400 v4',          'NZaXZXNZaXZaNNa'),
('24', 'Сетевая карта D-Link DFE-520TX',       'ZNaNNNaAXA'),
('25', 'Сетевая карта D-Link DGE-528T',        'aNZANZZNAaaa'),
('26', 'Сетевая карта D-Link DGE-530',         'AZAAAXXNXaX'),
('27', 'Сетевая карта D-Link DGE-560T',        'XaZAANZAXNXX'),
('28', 'Сетевая карта TP-LINK TG-3468',        'aNNANAXZXAZAN'),
('29', 'Сетевая карта TP-LINK UE200',          'aZNANXAZAZZaaAa'),
('30', 'Сетевая карта TP-LINK UE300',          'ZNZXNXXZZNXA');


/*
    Заполнение списка самого оборудования
*/
INSERT INTO Hardware (HardwareId, TypeId, SerialNum) VALUES
('1',    '1',   '8a6VN_x-@hY2_'),
('2',    '1',   '3r8HZ@l@_oI9@'),
('3',    '1',   '9v0C0-z--hZ0-'),
('4',    '1',   '2q5Q2@u@-hK5@'),
('5',    '1',   '4u9X6-o@@nXT@'),
('6',    '2',   'p_@8g@NpWn_0R8VO'),
('7',    '2',   'x_-3b_CcTj@2NQIA'),
('8',    '2',   'q-_1i@CeFo-6Z1ZF'),
('9',    '2',   's__2c_UjAb@0QICI'),
('10',   '2',   'm-@4k@EiYz-4D1PQ'),
('11',   '3',   '2F28gIVtqQLkk-S'),
('12',   '3',   '1H65pDLbbBYgv-5'),
('13',   '3',   '6T89sNCloAGjw@A'),
('14',   '4',   '223FxDnY8_@4W4'),
('15',   '4',   'Q27YdMuL0-_9B9'),
('16',   '4',   '248PmDt41-_9WM'),
('17',   '5',   '91_dp2P@MN15-'),
('18',   '5',   '64-ycAL_Z08T-'),
('19',   '5',   '55_sc2I_OX6F@'),
('20',   '6',   '_@5126GYf8ZX_0'),
('21',   '6',   '_@24S3UPp1BT_5'),
('22',   '6',   '@-43PXFIc7FV-6'),
('23',   '6',   '@@79FH6Sm2JQ_3'),
('24',   '6',   '_@83X7AVm91Z_9'),
('25',   '6',   '_@90G8RWd3QE@9'),
('26',   '6',   '@_68S58Gz9V5-0'),
('27',   '7',   '@Nl0Gx@v6vH'),
('28',   '8',   '@@5Is9YGUb'),
('29',   '8',   '__EEw7VX3q'),
('30',   '8',   '-@5Pn2VX8g'),
('31',   '9',   'LSs@doRGC_'),
('32',   '9',   'VRf_zzDNF_'),
('33',   '10',  '95@6sb7PZnV'),
('34',   '10',  '0U-5zs4PVdR'),
('35',   '10',  '4P_8ag82BaU'),
('36',   '10',  '5W_5xx86AqD'),
('37',   '10',  '0F-0mi7RXuX'),
('38',   '11',  'Dg5B-04x9k7'),
('39',   '11',  'Dn5E@10j8k6'),
('40',   '12',  'DG1@-5-6_@'),
('41',   '12',  'SZT_@W@5--'),
('42',   '12',  'ESS__6_6@_'),
('43',   '13',  '5mECK@31Qg875_'),
('44',   '13',  '2pQTK@O4PvB96_'),
('45',   '13',  '4oVRQ-B2QvO92-'),
('46',   '14',  'M4dI6N1AH0ZE0xK'),
('47',   '14',  'N4vDY9WVR78H1xC'),
('48',   '14',  'E6zEIVHTS6ES8hF'),
('49',   '14',  '82bWPQEVO69I8o8'),
('50',   '14',  'V7gW5Z1CC2NE3xB'),
('51',   '15',  '6V1ROU82-QBMU1'),
('52',   '15',  'AMVFQP00@ADWWI'),
('53',   '15',  '2LTRZK95-UYMN9'),
('54',   '15',  'QPKO6B46-X1CWE'),
('55',   '15',  'YYKHPJ79@MNOQV'),
('56',   '16',  '0_999mU2F6-'),
('57',   '16',  '0_964aF3KI_'),
('58',   '16',  '3@658tX4UO-'),
('59',   '16',  '9-310aZ0PU_'),
('60',   '16',  '8_150eR0OI_'),
('61',   '17',  'YUcq2-yJ-Kj-W8'),
('62',   '17',  'FIye7_jZ-Dw-W4'),
('63',   '17',  'UFcz3@f6_As_P4'),
('64',   '18',  'h_hVh7jA6@GLu'),
('65',   '18',  'b@gSo2yW9@CYg'),
('66',   '18',  'x-fJu8iL9@OZr'),
('67',   '18',  'g_kQz6sP1-27r'),
('68',   '18',  'd_qXk8uS8_70r'),
('69',   '18',  'y-iUa6xV9-X0m'),
('70',   '19',  '22_RmZf@FHP'),
('71',   '19',  '07@ZwWm@KRX'),
('72',   '19',  '17@PuSu-0XU'),
('73',   '20',  '0ZOL99f18_BEF'),
('74',   '20',  '9ZFPO0z36-I9E'),
('75',   '20',  '3INLS2r34_SQ2'),
('76',   '20',  '1ILGJ0g60-UF6'),
('77',   '22',  '_Bf@W2F_4TTG83'),
('78',   '22',  '_Yk@I4P-0SLL69'),
('79',   '23',  '8@t2_R1@wL-h63p'),
('80',   '23',  '8@qD_96@g8_v14x'),
('81',   '24',  '_1x586qVMJ'),
('82',   '24',  '-6z828yRNN'),
('83',   '24',  '-0u045pPJD'),
('84',   '24',  '@8r042gLYQ'),
('85',   '25',  'd6-G0_@2Xivg'),
('86',   '25',  'w7-X8_-4Zkcj'),
('87',   '25',  'x5@I0@@7Jydh'),
('88',   '26',  'Z-RLP0H3YgS'),
('89',   '26',  'D-DSXA84Ic6'),
('90',   '26',  'B-BQPQP9VlX'),
('91',   '26',  'P@CINMA8Yq5'),
('92',   '27',  'Se-ER0_T93LT'),
('93',   '27',  '7n@US4_JI82I'),
('94',   '28',  'a70Y4HR-LL_C2'),
('95',   '28',  's43M2YJ-AM-V8'),
('96',   '28',  'p56O1PW-0E-F4'),
('97',   '29',  'm_9Y02I@Z-@dkAa'),
('98',   '30',  '-8@X26N__49L'),
('99',   '30',  '_7-53H1@@6HV'),
('100',  '30',  '_3_M1K2@@2QO');
