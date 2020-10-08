//const axios = require('axios');

// Область вывода уведомлений в диалоговом окне
var modalAlerts = document.getElementById("ModalAlerts");
// Область вывода уведомлений на самой странице
var pageAlerts = document.getElementById("PageAlerts");
// Таблица для вывода списка оборудования
var hardwareTable = document.getElementById("HardwareList");

// Форма добавления нового оборудования
var newHardwareForm = document.getElementById("ModalForm");

// Выбор типа оборудования
var hwTypeSelect = document.getElementById("hw-type");
// Поле ввода серийного номера оборудования
var hwSerialNumber = document.getElementById("hw-serial-number");
// Область вывода маски серийного номера
var serialNumberMask = document.getElementById("hw-sn-mask");
// Кнопка отправки формы
var submitBtn = document.getElementById("ModalFormSubmit");

// Массив типов оборудования
var hardwareTypes;
// Текущий тип оборудования
var selectedType;



/*
	Главная процедура
*/
function Main() {
	LoadHardwareList();
	LoadHardwareTypes();
	
	hwTypeSelect.onchange = function(evt) {
		var index = hwTypeSelect.selectedIndex;
		selectedType  = hardwareTypes[index];
		hwSerialNumber.maxLength = selectedType.serial_mask.length;
		serialNumberMask.innerText = selectedType.serial_mask;
	}
	
	newHardwareForm.onsubmit = function(evt) {
		SubmitNewHardware();
		return false;
	}
}


/*
	Процедура отправки записи нового оборудования
*/
function SubmitNewHardware() {
	var serial_num = hwSerialNumber.value;
	var serial_mask = selectedType.serial_mask;
	
	if (!CheckSerialNum(serial_mask, serial_num)) {
		ModalShowError("Ошибка: Введённый серийный номер не соответствует маске ввода!");
		return false;
	}
	axios.post('/data/hardware', {
		action: 'add',
		data: {
			hw_type_id: selectedType.type_id,
			hw_serial_num: serial_num
		}
	})
	.then(res => HandleSubmitResponse(res.data))
	.catch(err => ModalShowError("Ошибка отправки данных!"));
}


/*
	Процедура проверки серийного номера по маске
*/
function CheckSerialNum(mask, serial_num) {
	var test_regex = MakeRegExpByMask(mask);
	return test_regex.test(serial_num);
}


/*
	Процедура обработки ответа запроса на добавление записи
*/
function HandleSubmitResponse(response) {
	if (response.status == "success") {
		PageShowInfo(response.message);
		DismissModal();
	}
	if (response.status == "error") {
		ModalShowError("Ошибка: оборудование с таким серийным номером уже есть в базе данных");
	}
}


/*
	Процедура закрытия и сброса диалогового окна
*/
function DismissModal() {
	var entry = {
		hw_id: "Н/Д",
		hw_type: selectedType,
		serial_num: hwSerialNumber.value
	};
	AddToTable(entry);
	
	$('#AddHardwareDialog').modal('hide');
	$('#hw-type').val('default').selectpicker("refresh");
	serialNumberMask.innerText = selectedType.serial_mask;
	modalAlerts.innerHTML = "";
	newHardwareForm.reset();
}


/*
	Процедура получения регулярного выражения по маске
*/
function MakeRegExpByMask(mask) {
	
	var pattern = "";
	
	for (var i = 0; i < mask.length; i++) {
		switch (mask.charAt(i)) {
			case 'N':
				pattern = pattern + "[0-9]";
				break;
			case 'A':
				pattern = pattern + "[A-Z]";
				break;
			case 'a':
				pattern = pattern + "[a-z]";
				break;
			case 'X':
				pattern = pattern + "([A-Z]|[0-9])";
				break;
			case 'Z':
				pattern = pattern + "[-_@]";
				break;
			default:
				break;
		}
	}
	
	return new RegExp(pattern);
}


/*
	Процедура загрузки списка оборудования
*/
function LoadHardwareTypes() {
	axios.get("/data/hardware_types")
		.then(function(response) {
			hardwareTypes = Object.values(response.data);
			PopulateTypesList(hardwareTypes);
		})
		.catch(err => PageShowError("Ошибка загрузки списка типов оборудования!"));
}


/*
	Процедура заполнения селектора типов оборудования
*/
function PopulateTypesList(types) {
	
	hwTypeSelect.innerHTML = "";
	
	for (type of types) {
		var opt = document.createElement("option");
		opt.value       = type.type_id;
		opt.textContent = type.type_name;
		opt.setAttribute('data-tokens', type.type_name);
		hwTypeSelect.appendChild(opt);
	}
	
	selectedType = types[0];
	
	$('#hw-type').selectpicker('refresh');
}


/*
	Процедура загрузки списка оборудования
*/
function LoadHardwareList() {
	axios.get("/data/hardware")
		.then(response => PopulateTable(response.data))
		.catch(err => PageShowError("Ошибка загрузки списка оборудования!"));
}


/*
	Процедура заполнения таблицы
*/
function PopulateTable(data) {
	
	var entries = Object.values(data);
	var tableBody = hardwareTable.getElementsByTagName("tbody")[0];
	
	tableBody.innerHTML = "";
	
	for (entry of entries) {
		var newRow = tableBody.insertRow(-1);
		newRow.insertCell().innerText = entry.hw_id;
		newRow.insertCell().innerText = entry.hw_type.type_name;
		newRow.insertCell().innerText = entry.serial_num;
	}
}


/*
	Процедура добавления записи в таблицу
*/
function AddToTable(entry) {
	var tableBody = hardwareTable.getElementsByTagName("tbody")[0];
	var newRow = tableBody.insertRow(0);
	newRow.className = "success";
	newRow.insertCell().innerText = entry.hw_id;
	newRow.insertCell().innerText = entry.hw_type.type_name;
	newRow.insertCell().innerText = entry.serial_num;
}


/*
	Процедура вывода уведомления на странице
*/
function PageShowInfo(message) {
	ShowAlert(pageAlerts, message, "info")
}


/*
	Процедура вывода уведомления об ошибке на странице
*/
function PageShowError(message) {
	ShowAlert(pageAlerts, message, "danger")
}


/*
	Процедура вывода уведомления об ошибке в диалоговом окне
*/
function ModalShowInfo(message) {
	ShowAlert(modalAlerts, message, "info")
}


/*
	Процедура вывода уведомления об ошибке в диалоговом окне
*/
function ModalShowError(message) {
	ShowAlert(modalAlerts, message, "danger")
}


/*
	Процедура вывода уведомления в указанной области
*/
function ShowAlert(page_area, message, type) {
	var content = page_area.innerHTML;
	page_area.innerHTML = GetAlertTmpl(message, type) + content;
}


/*
	Шаблон для уведомления
*/
function GetAlertTmpl(message, type)
{
	return `
		<div class="alert alert-${type} alert-dismissible" role="alert">
			<button type="button" class="close" data-dismiss="alert"><span>&times;</span></button>
			${message}
		</div>
	`;
}


/*
	Вызов главной функции
*/
Main();
