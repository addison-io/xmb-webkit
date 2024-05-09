$(document).ready(function() {
	$('.game-bar img').click(function() {
		$.ajax({
            type: 'POST',
            url: run_rom_path,
            headers: {
                "X-CSRFToken": $('meta[name="csrf-token"]').attr('content')
            },
            data: {
            	rom: $(this).data('rom'),
				iso: $(this).data('iso'),
			},
            success: function (response) {
            }
        });
	});
    
    var active_rom_index = -1;
    var active_game_index = 0;
    var init_active_game_index = 2;

    var play_game_timeout = null;
    var scroll_sidebar_description_timeout = null;

    var rom_bar_left_target = 0;
    var slide_rom_bar_doing = false;
    var game_bar_top_target = 0;
    var game_bar_top_init = false;
    var slide_game_bar_doing = false;

    function play_tick() {
      var tick_audio = new Audio(tick_song_path);
      tick_audio.play();
    }

    function slideRomBar() {
        var rom_bar_left = parseInt($('.display-bar .rom-bar').css('left'));
        if (rom_bar_left < rom_bar_left_target) {
            rom_bar_left = rom_bar_left + 1;
        } else if (rom_bar_left > rom_bar_left_target) {
            rom_bar_left = rom_bar_left - 1;
        }
        $('.display-bar .rom-bar').css('left', rom_bar_left + 'px');
        if (parseInt(rom_bar_left) != parseInt(rom_bar_left_target)) {
            slide_rom_bar_doing = true;
            setTimeout(function() {
                slideRomBar();
            }, 1);
        } else {
            slide_rom_bar_doing = false;
        }
    }
    function slideGameBar() {
        var game_bar_top = parseInt($('.display-bar .game-bar').css('top'));
        var slide_game_step = 1;
        if (game_bar_top_init) {
            slide_game_step = 10;
        }
        if (game_bar_top < game_bar_top_target) {
            game_bar_top = game_bar_top + slide_game_step;
            if (game_bar_top > game_bar_top_target) {
                game_bar_top = game_bar_top_target;
            }
        } else if (game_bar_top > game_bar_top_target) {
            game_bar_top = game_bar_top - slide_game_step;
            if (game_bar_top < game_bar_top_target) {
                game_bar_top = game_bar_top_target;
            }
        }
        $('.display-bar .game-bar').css('top', game_bar_top + 'px');
        if (parseInt(game_bar_top) != parseInt(game_bar_top_target)) {
            slide_game_bar_doing = true;
            setTimeout(function() {
                slideGameBar();
            }, 1);
        } else {            
            slide_game_bar_doing = false;
        }
    }

    function initRom() {
        var rom_items = $('.display-bar .rom-bar .rom-item');
        var middle_rom_index = 1;
        if (window.innerWidth >= 768) {
           middle_rom_index = init_active_game_index;
        }
        $('.display-bar .game-bar').css('left', ($(rom_items[0]).width() * (middle_rom_index + 1.25)) + 'px');
    }
    initRom();

    function activeRom() {
        var rom_items = $('.display-bar .rom-bar .rom-item');
        var middle_rom_index = 1;
        if (window.innerWidth >= 768) {
            middle_rom_index = init_active_game_index;
        }
        rom_bar_left_target = $(rom_items[0]).width() * (middle_rom_index - active_rom_index) * 2
        slideRomBar();

        var rom = '';
        for (var rom_index = 0; rom_index < rom_items.length; rom_index++) {
            var rom_item = $(rom_items[rom_index]);
            if (rom_index == active_rom_index) {
                rom = rom_item.data('rom');
                rom_item.addClass('active');
            } else {
                rom_item.removeClass('active');
            }
        }
        var active_rom_game_count = 0;
        var game_lists = $('.game-bar .game-list');
        for (var game_list_index = 0; game_list_index < game_lists.length; game_list_index++) {
            var game_list = $(game_lists[game_list_index]);
            if (game_list.data('rom') == rom) {
                game_list.addClass('active');
                active_rom_game_count = game_list.find('.game-item').length;
            } else {
                game_list.removeClass('active');
            }
        }
        if (active_rom_game_count > init_active_game_index) {
            active_game_index = init_active_game_index;
        } else {
            active_game_index = active_rom_game_count - 1;            
        }
        if (active_rom_game_count) {
            $('.side-bar').addClass('show');
        } else {
            $('.side-bar').removeClass('show');
        }
        activeGame(true);
    }
    function stopGameVideo() {        
        var active_game_item = $('.display-bar .game-list.active .game-item.active');
        if (active_game_item.find('.game-item-video source') && active_game_item.find('.game-item-video source').length) {
            active_game_item.find('.game-item-img').show();
            active_game_item.find('.game-item-video').hide();
            active_game_item.find('.game-item-video').trigger('pause');
        }
    }
    function playGameVideo(game_index) {
        if (active_game_index == game_index) {
            var active_game_item = $('.display-bar .game-list.active .game-item.active');
            if (active_game_item.find('.game-item-video source') && active_game_item.find('.game-item-video source').length) {
                active_game_item.find('.game-item-img').hide();
                active_game_item.find('.game-item-video').show();
                active_game_item.find('.game-item-video').trigger('play');

                active_game_item.find('.game-item-video')[0].addEventListener('ended', function(e) {
                    stopGameVideo();
                }, false);
            }
        }
    }
    function scrollSidebarDescription(game_index) {
        if (active_game_index == game_index) {
            if (scroll_sidebar_description_timeout) {
                clearTimeout(scroll_sidebar_description_timeout);
                scroll_sidebar_description_timeout = null;
            }

            var side_bar_bottom = $('.side-bar .side-bar-bottom');
            var side_bar_bottom_height = side_bar_bottom.height();
            var game_description = $('.side-bar .item-description');
            var game_description_height = game_description.height();
            if (side_bar_bottom_height < game_description_height) {
                var game_description_margin_top = parseInt(game_description.css('margin-top'));
                if (game_description_margin_top - 1 + game_description_height > side_bar_bottom_height) {
                    game_description_margin_top = game_description_margin_top - 1;
                } else {
                    game_description_margin_top = 0;                
                }
                $('.side-bar .item-description').css('margin-top', game_description_margin_top + 'px');
                if (game_description_margin_top) {
                    side_bar_bottom.addClass('scroll');
                    scroll_sidebar_description_timeout = setTimeout(function() {
                        scrollSidebarDescription(game_index);
                    }, 100);
                } else {
                    side_bar_bottom.removeClass('scroll');
                    scroll_sidebar_description_timeout = setTimeout(function() {
                        scrollSidebarDescription(game_index);
                    }, 1000 * 5);
                }
            }
        }
    }

    function activeGame(init = false) {
        $('.side-bar .item-img').attr('src', '');
        $('.side-bar .item-name').html('');
        $('.side-bar .item-year').html('');
        $('.side-bar .item-description').html('');
        $('.side-bar .item-description').css('margin-top', '0px');
        $('.side-bar .side-bar-bottom').removeClass('scroll');

        if (play_game_timeout) {
            clearTimeout(play_game_timeout);
            play_game_timeout = null;
        }
        if (scroll_sidebar_description_timeout) {
            clearTimeout(scroll_sidebar_description_timeout);
            scroll_sidebar_description_timeout = null;
        }

        var active_rom_item = $('.display-bar .rom-bar .rom-item.active');
        rom_item_height = active_rom_item.height();
        var game_list = $('.game-bar .game-list.active');
        var active_rom_game_count = game_list.find('.game-item').length;
        var game_items = game_list.find('.game-item');
        for (var game_item_index = 0; game_item_index < game_items.length; game_item_index++) {
            var game_item = $(game_items[game_item_index]);
            if (game_item_index == active_game_index) {
                game_item.addClass('active');

                game_item.css('margin-top', (rom_item_height * 2.5) + 'px');
                $('.side-bar .item-img').attr('src', game_item.data('image'));
                $('.side-bar .item-name').html(game_item.find('.game-item-name').html());
                $('.side-bar .item-year').html(game_item.data('year'));
                $('.side-bar .item-description').html(game_item.data('description'));
            } else {
                game_item.removeClass('active');

                game_item.css('margin-top', '15px');
            }
            if (game_item.find('.game-item-video source') && game_item.find('.game-item-video source').length) {
                game_item.find('.game-item-img').show();
                game_item.find('.game-item-video').hide();
                game_item.find('.game-item-video').trigger('pause');
            }
        }

        var normal_game_item = $('.display-bar .game-bar .game-item:not(.active)')[0];
        var normal_game_height = $(normal_game_item).height() + parseInt($(normal_game_item).css('margin-bottom'));
        var game_bar_top = (init_active_game_index - active_game_index) * normal_game_height + $('.display-bar .rom-bar').height() - rom_item_height * 1.5;
        if (game_items.length) {
            game_bar_top = game_bar_top + parseInt($('.display-bar .rom-bar').css('top')) - normal_game_height * init_active_game_index;
        }
        game_bar_top_target = game_bar_top;
        game_bar_top_init = init;
        slideGameBar();

        var play_active_game_index = active_game_index;
        play_game_timeout = setTimeout(function() {
            playGameVideo(play_active_game_index);
        }, 1000 * 10);
        scroll_sidebar_description_timeout = setTimeout(function() {
            scrollSidebarDescription(play_active_game_index);
        }, 1000 * 5);
    }

    $(document).keydown(function (event) {
        if (event.which == 27) {
            $.ajax({
                type: 'GET',
                url: exit_path,
                headers: {
                    "Access-Control-Allow-Origin": '*'
                },
                data: {},
                success: function (response) { }
            });
        } else {
            if (active_rom_index == -1) {
                if (event.which == 38 || event.which == 37 || event.which == 40 || event.which == 39 || event.which == 13) {
                    active_rom_index = 0;
                    activeRom();
                    play_tick();
                }
            } else {
                if (event.which == 38 || event.which == 37 || event.which == 40 || event.which == 39 || event.which == 13) {
                    stopGameVideo();
                    play_tick();
                }
                if (event.which == 38) { // KeyUp
                    if (active_game_index) {
                        active_game_index = active_game_index - 1;
                    }
                    activeGame();
                } else if (event.which == 37) { // KeyLeft
                    if (active_rom_index) {
                        active_rom_index = active_rom_index - 1;
                    }
                    activeRom();
                } else if (event.which == 40) { // KeyDown
                    var game_items = $('.display-bar .game-bar .game-list.active .game-item');
                    if (active_game_index + 1 < game_items.length) {
                        active_game_index = active_game_index + 1;
                    }
                    activeGame();
                } else if (event.which == 39) { // KeyRight
                    var rom_items = $('.display-bar .rom-bar .rom-item');
                    if (active_rom_index + 1 < rom_items.length) {
                        active_rom_index = active_rom_index + 1;
                    }
                    activeRom();
                } else if (event.which == 13) { // Enter            
                    var active_game_item = $('.display-bar .game-bar .game-list.active .game-item.active');
                    if (play_game_timeout) {
                        clearTimeout(play_game_timeout);
                        play_game_timeout = null;
                    }
                    $.ajax({
                        type: 'GET',
                        url: run_rom_path,
                        headers: {
                            "Access-Control-Allow-Origin": '*'
                        },
                        data: {
                            rom: active_game_item.data('rom'),
                            iso: active_game_item.data('iso'),
                            name: active_game_item.data('name'),
                        },
                        success: function (response) {
                        }
                    });
                }
            }
        }
    });
});