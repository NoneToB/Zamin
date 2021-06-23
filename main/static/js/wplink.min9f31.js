/*! This file is auto-generated */
!function(s,l,o){var c,e,t,n,i,h=/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63}$/i,u=/^(https?|ftp):\/\/[A-Z0-9.-]+\.[A-Z]{2,63}[^ "]*$/i,p={},a={},r="ontouchend"in document;function d(){return c?c.$('a[data-wplink-edit="true"]'):null}window.wpLink={timeToTriggerRiver:150,minRiverAJAXDuration:200,riverBottomThreshold:5,keySensitivity:100,lastSearch:"",textarea:"",modalOpen:!1,init:function(){p.wrap=s("#wp-link-wrap"),p.dialog=s("#wp-link"),p.backdrop=s("#wp-link-backdrop"),p.submit=s("#wp-link-submit"),p.close=s("#wp-link-close"),p.text=s("#wp-link-text"),p.url=s("#wp-link-url"),p.nonce=s("#_ajax_linking_nonce"),p.openInNewTab=s("#wp-link-target"),p.search=s("#wp-link-search"),a.search=new t(s("#search-results")),a.recent=new t(s("#most-recent-results")),a.elements=p.dialog.find(".query-results"),p.queryNotice=s("#query-notice-message"),p.queryNoticeTextDefault=p.queryNotice.find(".query-notice-default"),p.queryNoticeTextHint=p.queryNotice.find(".query-notice-hint"),p.dialog.on("keydown",wpLink.keydown),p.dialog.on("keyup",wpLink.keyup),p.submit.on("click",function(e){e.preventDefault(),wpLink.update()}),p.close.add(p.backdrop).add("#wp-link-cancel button").on("click",function(e){e.preventDefault(),wpLink.close()}),a.elements.on("river-select",wpLink.updateFields),p.search.on("focus.wplink",function(){p.queryNoticeTextDefault.hide(),p.queryNoticeTextHint.removeClass("screen-reader-text").show()}).on("blur.wplink",function(){p.queryNoticeTextDefault.show(),p.queryNoticeTextHint.addClass("screen-reader-text").hide()}),p.search.on("keyup input",function(){window.clearTimeout(e),e=window.setTimeout(function(){wpLink.searchInternalLinks()},500)}),p.url.on("paste",function(){setTimeout(wpLink.correctURL,0)}),p.url.on("blur",wpLink.correctURL)},correctURL:function(){var e=s.trim(p.url.val());e&&i!==e&&!/^(?:[a-z]+:|#|\?|\.|\/)/.test(e)&&(p.url.val("http://"+e),i=e)},open:function(e,t,n){var i=s(document.body);i.addClass("modal-open"),wpLink.modalOpen=!0,wpLink.range=null,e&&(window.wpActiveEditor=e),window.wpActiveEditor&&(this.textarea=s("#"+window.wpActiveEditor).get(0),void 0!==window.tinymce&&(i.append(p.backdrop,p.wrap),i=window.tinymce.get(window.wpActiveEditor),c=i&&!i.isHidden()?i:null),!wpLink.isMCE()&&document.selection&&(this.textarea.focus(),this.range=document.selection.createRange()),p.wrap.show(),p.backdrop.show(),wpLink.refresh(t,n),s(document).trigger("wplink-open",p.wrap))},isMCE:function(){return c&&!c.isHidden()},refresh:function(e,t){a.search.refresh(),a.recent.refresh(),wpLink.isMCE()?wpLink.mceRefresh(e,t):(p.wrap.hasClass("has-text-field")||p.wrap.addClass("has-text-field"),document.selection?document.selection.createRange().text:void 0!==this.textarea.selectionStart&&this.textarea.selectionStart!==this.textarea.selectionEnd&&(t=this.textarea.value.substring(this.textarea.selectionStart,this.textarea.selectionEnd)||t||""),p.text.val(t),wpLink.setDefaultValues()),r?p.url.trigger("focus").trigger("blur"):window.setTimeout(function(){p.url[0].select(),p.url.trigger("focus")}),a.recent.ul.children().length||a.recent.ajax(),i=p.url.val().replace(/^http:\/\//,"")},hasSelectedText:function(e){var t,n,i,a=c.selection.getContent();if(/</.test(a)&&(!/^<a [^>]+>[^<]+<\/a>$/.test(a)||-1===a.indexOf("href=")))return!1;if(e.length){if(!(n=e[0].childNodes)||!n.length)return!1;for(i=n.length-1;0<=i;i--)if(3!=(t=n[i]).nodeType&&!window.tinymce.dom.BookmarkManager.isBookmarkNode(t))return!1}return!0},mceRefresh:function(e,t){var n,i,a=d(),r=this.hasSelectedText(a);a.length?(n=a.text(),i=a.attr("href"),s.trim(n)||(n=t||""),"_wp_link_placeholder"!==(i=e&&(u.test(e)||h.test(e))?e:i)?(p.url.val(i),p.openInNewTab.prop("checked","_blank"===a.attr("target")),p.submit.val(l.update)):this.setDefaultValues(n),e&&e!==i?p.search.val(e):p.search.val(""),window.setTimeout(function(){wpLink.searchInternalLinks()})):(n=c.selection.getContent({format:"text"})||t||"",this.setDefaultValues(n)),r?(p.text.val(n),p.wrap.addClass("has-text-field")):(p.text.val(""),p.wrap.removeClass("has-text-field"))},close:function(e){s(document.body).removeClass("modal-open"),wpLink.modalOpen=!1,"noReset"!==e&&(wpLink.isMCE()?(c.plugins.wplink&&c.plugins.wplink.close(),c.focus()):(wpLink.textarea.focus(),wpLink.range&&(wpLink.range.moveToBookmark(wpLink.range.getBookmark()),wpLink.range.select()))),p.backdrop.hide(),p.wrap.hide(),i=!1,s(document).trigger("wplink-close",p.wrap)},getAttrs:function(){return wpLink.correctURL(),{href:s.trim(p.url.val()),target:p.openInNewTab.prop("checked")?"_blank":null}},buildHtml:function(e){var t='<a href="'+e.href+'"';return e.target&&(t+=' rel="noopener" target="'+e.target+'"'),t+">"},update:function(){wpLink.isMCE()?wpLink.mceUpdate():wpLink.htmlUpdate()},htmlUpdate:function(){var e,t,n,i,a,r=wpLink.textarea;r&&(n=wpLink.getAttrs(),i=p.text.val(),(a=document.createElement("a")).href=n.href,"javascript:"!==a.protocol&&"data:"!==a.protocol||(n.href=""),n.href&&(e=wpLink.buildHtml(n),document.selection&&wpLink.range?(r.focus(),wpLink.range.text=e+(i||wpLink.range.text)+"</a>",wpLink.range.moveToBookmark(wpLink.range.getBookmark()),wpLink.range.select(),wpLink.range=null):void 0!==r.selectionStart&&(t=r.selectionStart,a=r.selectionEnd,i=t+(e=e+(n=i||r.value.substring(t,a))+"</a>").length,t!==a||n||(i-=4),r.value=r.value.substring(0,t)+e+r.value.substring(a,r.value.length),r.selectionStart=r.selectionEnd=i),wpLink.close(),r.focus(),s(r).trigger("change"),o.a11y.speak(l.linkInserted)))},mceUpdate:function(){var e,t,n,i=wpLink.getAttrs(),a=document.createElement("a");if(a.href=i.href,"javascript:"!==a.protocol&&"data:"!==a.protocol||(i.href=""),!i.href)return c.execCommand("unlink"),void wpLink.close();e=d(),c.undoManager.transact(function(){e.length||(c.execCommand("mceInsertLink",!1,{href:"_wp_link_placeholder","data-wp-temp-link":1}),e=c.$('a[data-wp-temp-link="1"]').removeAttr("data-wp-temp-link"),n=s.trim(e.text())),e.length?(p.wrap.hasClass("has-text-field")&&((t=p.text.val())?e.text(t):n||e.text(i.href)),i["data-wplink-edit"]=null,i["data-mce-href"]=i.href,e.attr(i)):c.execCommand("unlink")}),wpLink.close("noReset"),c.focus(),e.length&&(c.selection.select(e[0]),c.plugins.wplink&&c.plugins.wplink.checkLink(e[0])),c.nodeChanged(),o.a11y.speak(l.linkInserted)},updateFields:function(e,t){p.url.val(t.children(".item-permalink").val()),p.wrap.hasClass("has-text-field")&&!p.text.val()&&p.text.val(t.children(".item-title").text())},getUrlFromSelection:function(e){return e||(this.isMCE()?e=c.selection.getContent({format:"text"}):document.selection&&wpLink.range?e=wpLink.range.text:void 0!==this.textarea.selectionStart&&(e=this.textarea.value.substring(this.textarea.selectionStart,this.textarea.selectionEnd))),(e=s.trim(e))&&h.test(e)?"mailto:"+e:e&&u.test(e)?e.replace(/&amp;|&#0?38;/gi,"&"):""},setDefaultValues:function(e){p.url.val(this.getUrlFromSelection(e)),p.search.val(""),wpLink.searchInternalLinks(),p.submit.val(l.save)},searchInternalLinks:function(){var e,t=p.search.val()||"",n=parseInt(l.minInputLength,10)||3;t.length>=n?(a.recent.hide(),a.search.show(),wpLink.lastSearch!=t&&(wpLink.lastSearch=t,e=p.search.parent().find(".spinner").addClass("is-active"),a.search.change(t),a.search.ajax(function(){e.removeClass("is-active")}))):(a.search.hide(),a.recent.show())},next:function(){a.search.next(),a.recent.next()},prev:function(){a.search.prev(),a.recent.prev()},keydown:function(e){var t;27===e.keyCode?(wpLink.close(),e.stopImmediatePropagation()):9===e.keyCode&&("wp-link-submit"!==(t=e.target.id)||e.shiftKey?"wp-link-close"===t&&e.shiftKey&&(p.submit.trigger("focus"),e.preventDefault()):(p.close.trigger("focus"),e.preventDefault())),e.shiftKey||38!==e.keyCode&&40!==e.keyCode||document.activeElement&&("link-title-field"===document.activeElement.id||"url-field"===document.activeElement.id)||(t=38===e.keyCode?"prev":"next",clearInterval(wpLink.keyInterval),wpLink[t](),wpLink.keyInterval=setInterval(wpLink[t],wpLink.keySensitivity),e.preventDefault())},keyup:function(e){38!==e.keyCode&&40!==e.keyCode||(clearInterval(wpLink.keyInterval),e.preventDefault())},delayedCallback:function(e,t){var n,i,a,r;return t?(setTimeout(function(){return i?e.apply(r,a):void(n=!0)},t),function(){if(n)return e.apply(this,arguments);a=arguments,r=this,i=!0}):e}},t=function(e,t){var n=this;this.element=e,this.ul=e.children("ul"),this.contentHeight=e.children("#link-selector-height"),this.waiting=e.find(".river-waiting"),this.change(t),this.refresh(),s("#wp-link .query-results, #wp-link #link-selector").on("scroll",function(){n.maybeLoad()}),e.on("click","li",function(e){n.select(s(this),e)})},s.extend(t.prototype,{refresh:function(){this.deselect(),this.visible=this.element.is(":visible")},show:function(){this.visible||(this.deselect(),this.element.show(),this.visible=!0)},hide:function(){this.element.hide(),this.visible=!1},select:function(e,t){var n,i,a,r;e.hasClass("unselectable")||e==this.selected||(this.deselect(),this.selected=e.addClass("selected"),n=e.outerHeight(),i=this.element.height(),a=e.position().top,r=this.element.scrollTop(),a<0?this.element.scrollTop(r+a):i<a+n&&this.element.scrollTop(r+a-i+n),this.element.trigger("river-select",[e,t,this]))},deselect:function(){this.selected&&this.selected.removeClass("selected"),this.selected=!1},prev:function(){var e;this.visible&&this.selected&&(e=this.selected.prev("li")).length&&this.select(e)},next:function(){var e;!this.visible||(e=this.selected?this.selected.next("li"):s("li:not(.unselectable):first",this.element)).length&&this.select(e)},ajax:function(n){var i=this,e=1==this.query.page?0:wpLink.minRiverAJAXDuration,e=wpLink.delayedCallback(function(e,t){i.process(e,t),n&&n(e,t)},e);this.query.ajax(e)},change:function(e){this.query&&this._search==e||(this._search=e,this.query=new n(e),this.element.scrollTop(0))},process:function(e,t){var n,i="",a=!0,t=1==t.page;e?s.each(e,function(){n=a?"alternate":"",n+=this.title?"":" no-title",i+=n?'<li class="'+n+'">':"<li>",i+='<input type="hidden" class="item-permalink" value="'+this.permalink+'" />',i+='<span class="item-title">',i+=this.title||l.noTitle,i+='</span><span class="item-info">'+this.info+"</span></li>",a=!a}):t&&(i+='<li class="unselectable no-matches-found"><span class="item-title"><em>'+l.noMatchesFound+"</em></span></li>"),this.ul[t?"html":"append"](i)},maybeLoad:function(){var n=this,i=this.element,e=i.scrollTop()+i.height();!this.query.ready()||e<this.contentHeight.height()-wpLink.riverBottomThreshold||setTimeout(function(){var e=i.scrollTop(),t=e+i.height();!n.query.ready()||t<n.contentHeight.height()-wpLink.riverBottomThreshold||(n.waiting.addClass("is-active"),i.scrollTop(e+n.waiting.outerHeight()),n.ajax(function(){n.waiting.removeClass("is-active")}))},wpLink.timeToTriggerRiver)}}),s.extend((n=function(e){this.page=1,this.allLoaded=!1,this.querying=!1,this.search=e}).prototype,{ready:function(){return!(this.querying||this.allLoaded)},ajax:function(t){var n=this,i={action:"wp-link-ajax",page:this.page,_ajax_linking_nonce:p.nonce.val()};this.search&&(i.search=this.search),this.querying=!0,s.post(window.ajaxurl,i,function(e){n.page++,n.querying=!1,n.allLoaded=!e,t(e,i)},"json")}}),s(document).ready(wpLink.init)}(jQuery,window.wpLinkL10n,window.wp);