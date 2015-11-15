
if (typeof jQuery !== 'undefined') {
    var onImagaUpload = function(files, editor, $editable) {

        var $form = $('.note-image-dialog .note-modal-form');

        $('<iframe id="fileupload" src="about:blank"  style="display: none;" name="docfile"></iframe>').appendTo('body');


        $.imageUploaded = function(image) {
            editor.insertImage($editable, image);
        };

        var csrftoken = $.cookie('csrftoken');

        $form.append('<input type="hidden" name="csrfmiddlewaretoken" value="' + csrftoken + '">');

        $form.attr({
            enctype: 'multipart/form-data',
            target: 'docfile',
            action: '/file/upload',
            method: 'post'
        });
        $form[0].submit();
    };

    (function($) {
        $.extend($.summernote.options, {
            lang: 'ko-KR',
            height: 300,                  // set editable area's height
            tabsize: 2,                   // size of tab
            placeholder: '내용을 입력해 주세요.', // set editable area's placeholder text
            prettifyHtml: false,
            disableLinkTarget: true,
            // toolbar
            toolbar: [
                ['style', ['style']],
                ['font', ['bold', 'italic', 'underline', 'strikethrough', 'clear']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'table']],
                ['insert', ['codeblock', 'link', 'picture', 'video', 'hr']],
                ['view', ['fullscreen', 'codeview', 'help']]
            ],
            onImageUpload : onImagaUpload
        });

        $.timeago.settings.strings = {
            suffixAgo: "전",
            suffixFromNow: "후",
            seconds: "방금",
            minute: "1분",
            minutes: "%d분",
            hour: "1시간",
            hours: "%d시간",
            day: "하루",
            days: "%d일",
            month: "한 달",
            months: "%d달",
            year: "1년",
            years: "%d년",
            wordSeparator: " "
        };
    })(jQuery);
}