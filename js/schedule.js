$(document).ready( function() {
  // For conference and workshop schedule
  //dateStr is expected in the format 2015-07-16", then returns "Thu Jul 16 2015"
  var getDateString = function(dateStr) {
    var year = parseInt(dateStr.substr(0, 4), 10);
    var month = parseInt(dateStr.substr(5, 2), 10) - 1;
    var day = parseInt(dateStr.substr(8, 2), 10);
    var d = new Date();
    d.setFullYear(year,month,day);
    return d.toDateString();
  }

  //dateString is expected in the format "2014-07-24T11:30:00Z" returns time "11:30"
  var getTimeString = function(dateString) {
    return dateString.substr(dateString.indexOf('T')+1,5);
  }

  var getHrMin = function(dateString) {
    var hr = dateString.substring(0, dateString.indexOf(":"));
    var min = dateString.substring(dateString.indexOf(":")+1);
    return [hr, min];
  }

  var getdateObject = function(hr, min) {
    var time = new Date();
    time.setHours(hr);
    time.setMinutes(min);
    return time;
  }

  var toTimeString = function(time) {
    return ((time.getHours() < 10 ? '0':'') + time.getHours()) + ':' + ((time.getMinutes() < 10 ? '0':'') + time.getMinutes());
  }

  //Input UTC, returns IST
  var getIST = function(utcTime) {
    var hr = parseInt(getHrMin(utcTime)[0], 10) + 5;
    var min = parseInt(getHrMin(utcTime)[1], 10) + 30;
    var time = getdateObject(hr, min);
    ist = toTimeString(time);
    return ist;
  }

  var createTable = function(schedule) {
    var hr;
    var min;
    var startTime;
    var endTime;
    var slots;
    var slotTime;
    hr = getHrMin(schedule.start)[0];
    min = getHrMin(schedule.start)[1];
    startTime = getdateObject(hr, min);
    hr = getHrMin(schedule.end)[0];
    min = getHrMin(schedule.end)[1];
    endTime = getdateObject(hr, min);
    schedule.slots = [];
    do {
      slotTime = toTimeString(startTime);
      schedule.slots.push({slot: slotTime, issession: false, sessions: [], occupied: "empty"});
      startTime.setMinutes(startTime.getMinutes() + 5);
    }while(startTime <= endTime);
  }

  var getTotalMins = function(time) {
    var hr = parseInt(getHrMin(time)[0], 10);
    var min = parseInt(getHrMin(time)[1], 10);
    return (hr * 60) + min;
  }

  var getAudiTitle = function(roomName) {
    return roomName.substring(roomName.indexOf('/')+1).replace(/-/g, ' ')  + ", " + roomName.substring(0, roomName.indexOf('/')).replace(/-/g, ' ');
  }

  //roomName is "nimhans-convention-center/audi-1" return "AUDI-1"
  var getShortAudiTitle = function(roomName) {
    return roomName.substring(roomName.indexOf('/')+1).replace(/-/g, ' ');
  }

  //audiName is AUDI-2 returns track 1.
  var getTrack = function(audiName, rooms) {
    var index;
    for (index=0; index<rooms.length; index++) {
      if (rooms[index].name === audiName) {
        return rooms[index].track;
      }
    }
  }

  var pushSessions = function(emptyschedule, datapoints) {
    //Check if each session ends within slot if not add rowspan
    datapoints.forEach(function(slot, slotindex, slots) {
    var sessions = slot.sessions;
    sessions.forEach(function(session, sessionindex, sessions) {
      var sessionTime = getTotalMins(session.start);
      var sessionEndTime = getTotalMins(session.end);
      emptyschedule.slots.forEach(function(emptyscheduleSlot, emptyscheduleSlotIndex, emptyscheduleSlots) {
        //Check if the session start time is equal to time interval
        if (getTotalMins(emptyscheduleSlot.slot) === sessionTime) {
          emptyscheduleSlots[emptyscheduleSlotIndex].sessions.push(session);
          emptyscheduleSlots[emptyscheduleSlotIndex].issession = true;
        }
      });//eof schedule.slots
    }); //eof sessions loop
  });//eof slots loop
  }

  var addRowSpan = function(schedule) {
    schedule.slots.forEach(function(slot, slotindex, slots) {
      if (slot.issession) {
        if (slot.sessions[0].track === 0 || slot.sessions[0].is_break) {
          slot.occupied = 0;
        }
        var sessions = slot.sessions;
        for(sessionindex = 0; sessionindex < sessions.length; sessionindex++) {
          var sessionEndTime = getTotalMins(sessions[sessionindex].end);
          var index = slotindex + 1;
          var rowspan = 1;
          var rows = false;
          for (index = slotindex + 1; index < slots.length; index++) {
            if (slots[index].issession === true && sessionEndTime <= getTotalMins(slots[index].sessions[0].start)) {
              break;
            }
            else if(slots[index].issession === true && sessionEndTime > getTotalMins(slots[index].sessions[0].start)) {
              rows = true;
              rowspan = rowspan + 1;
            }
          }
          if (rows) {
            schedule.slots[slotindex].sessions[sessionindex].rowspan = rowspan;
          }
        }
      }
    });//eof slots loop
  }

  var checkColumns = function(schedule) {
    //Check if session have track 0 to maintain table
    for(var counter = 0; counter < schedule.slots.length; counter++) {
      if (schedule.slots[counter].issession && schedule.slots[counter].occupied !== 0) {
        //Check previous session extends till this one
        var found = false;
        for(j=counter-1; j>0; j--) {
          if(schedule.slots[j].issession && getTotalMins(schedule.slots[j].sessions[0].end) > getTotalMins(schedule.slots[counter].sessions[0].start)) {
            found = true;
          }
        }
        if (found === false) {
          //Add a empty track session
          var hr = parseInt(getHrMin(schedule.slots[counter].sessions[0].start)[0], 10);
          var min = parseInt(getHrMin(schedule.slots[counter].sessions[0].start)[1], 10) + 5;
          var time = getdateObject(hr, min);
          var endTime = toTimeString(time);
          schedule.slots[counter].sessions[1] = schedule.slots[counter].sessions[0];
          schedule.slots[counter].sessions[0] = {track: 'empty', start: schedule.slots[counter].sessions[1].start, end: endTime};
        }
      }
    }
  }

  var renderResponsiveTable = function() {
    $('td.tab-active').attr('colspan', 3);
  }

  var disableResponsiveTable = function() {
    $('td').not('.centered').attr('colspan', "");
  }

  var renderScheduleTable = function(schedules, eventType, divContainer) {
    schedules.forEach(function(schedule) {
      var tableTemplate = $('#scheduletemplate').html();

      if (eventType === 'conference') {
        $(divContainer).append(Mustache.render(tableTemplate, schedule));
        $(".schedule-table-container p.loadingtxt").hide();
      }
      else {
        $(divContainer).append(Mustache.render(tableTemplate, schedule));
        $(".schedule-table-container p.loadingtxt").hide();
      }
    });
    if ($(window).width() < 768){
      renderResponsiveTable();
    }
  }

  function parseJson(data, eventType, divContainer) {
    var schedules = data.schedule;
    var workshopSchedule = [];
    var conferenceSchedule = [];
    var conferenceScheduleCounter = 0;
    var workshopScheduleCounter = 0;
    //Create rows at 5min intervals
    schedules.forEach(function(eachSchedule, scheduleindex, schedules) {
      var rooms = [];
      schedules[scheduleindex].date = getDateString(eachSchedule.date);
      schedules[scheduleindex].tableid = 'table-' + scheduleindex;

      //Type of schedule Conference/Workshop
      eachSchedule.slots.forEach(function(slot, slotindex, slots) {
        var sessions = slot.sessions;
        var startTime;
        var EndTime;
        //Start and end time in a schedule
        if (slotindex === 0) {
          schedules[scheduleindex].start = getIST(getTimeString(slot.sessions[0].start));
        }
        if (slotindex === slots.length-1) {
          schedules[scheduleindex].end = getIST(getTimeString(slot.sessions[sessions.length-1].end));
        }
        sessions.forEach(function(session, sessionindex, sessions) {
          //Tracks or No:of auditorium
          if (session.room && (rooms.indexOf(session.room) === -1)) {
              rooms.push(session.room);
          }
          //set IST time
          schedules[scheduleindex].slots[slotindex].sessions[sessionindex].start = getIST(getTimeString(session.start));
          schedules[scheduleindex].slots[slotindex].sessions[sessionindex].end = getIST(getTimeString(session.end));
        }); //eof sessions loop

        schedules[scheduleindex].type = 'conference';
      }); //eof schedule.slots loop

      //Sort rooms
      rooms.sort();

      //Add title and track to each room. Eg: room: "nimhans-convention-center/audi-1", title: "Audi 1", track: 0
      rooms.forEach(function(room, index, rooms) {
        rooms[index] = { name: room, title: getAudiTitle(room), shorttitle: getShortAudiTitle(room), track: index};
      });
      schedules[scheduleindex].rooms = rooms;

      //Add track based on room of the session eg: Audi 1 track 0, Audi 2 track 1
      eachSchedule.slots.forEach(function(slot, slotindex) {
        var sessions = slot.sessions;
        sessions.forEach(function(session, sessionindex) {
          if(session.room) {
            schedules[scheduleindex].slots[slotindex].sessions[sessionindex].track = getTrack(session.room, rooms);
            schedules[scheduleindex].slots[slotindex].sessions[sessionindex].roomTitle = getAudiTitle(session.room)
          }
        });
      });

      conferenceSchedule.push({date: schedules[scheduleindex].date, tableid: schedules[scheduleindex].tableid, rooms: schedules[scheduleindex].rooms, start: schedules[scheduleindex].start, end: schedules[scheduleindex].end});
      createTable(conferenceSchedule[conferenceScheduleCounter]);
      conferenceScheduleCounter += 1;
    });//eof schedules loop

    //Reset counters
    conferenceScheduleCounter = 0;
    workshopScheduleCounter = 0;

    schedules.forEach(function(schedule) {
      //Sort sessions based on track
      schedule.slots.forEach(function(slot, slotindex) {
        if (slot.sessions.length > 1) {
          slot.sessions.sort(function(session1, session2) {
              return session1.track - session2.track;
          });
        }
      });

      pushSessions(conferenceSchedule[conferenceScheduleCounter], schedule.slots);
      addRowSpan(conferenceSchedule[conferenceScheduleCounter]);
      checkColumns(conferenceSchedule[conferenceScheduleCounter]);
      conferenceScheduleCounter += 1;
    }); //eof schedules loop

    renderScheduleTable(conferenceSchedule, 'conference', divContainer);
  }

    $(window).resize(function() {
    if($(window).width() < 768) {
      renderResponsiveTable();
    }
    else{
      disableResponsiveTable();
    }
  });

  $('#event-schedule-table').on('click', 'table td .js-expand', function() {
    if($(this).hasClass('fa-caret-right')) {
      $(this).removeClass('fa-caret-right').addClass('fa-caret-down');
      $(this).parents('td').find('.description-text').slideDown();
    }
    else {
      $(this).removeClass('fa-caret-down').addClass('fa-caret-right');
      $(this).parents('td').find('.description-text').slideUp();
    }
  });

  $('#event-schedule-table').on('click', 'table th.js-track', function() {
    if($(window).width() < 768){
      var parentTable = $(this).parents('table');
      var activeColumn = $(this).attr('data-td');
      parentTable.find('.tab-active').removeClass('tab-active');
      $(this).addClass('tab-active');
      parentTable.find('.' + activeColumn).addClass('tab-active');
      renderResponsiveTable();
    }
  });

  if(($('.schedule-table-container').length)) {
    $.ajax({
      type: 'GET',
      dataType: 'json',
      url: window.EventDetails.schedule_url,
      success: function(data) {
        parseJson(data, window.EventDetails.schedule_type, '#event-schedule-table');
      }
    });//eof ajax call
  }

});
